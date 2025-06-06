import {useCallback, useEffect, useState} from "react"

import {useAtom} from "jotai"
import {useRouter} from "next/router"

import {getEnv} from "../dynamicEnv"
import {isDemo} from "../utils"

import {CLOUD_CONFIG, OSS_CONFIG} from "./assets/constants"
import {posthogAtom, type PostHogConfig} from "./store/atoms"
import {CustomPosthogProviderType} from "./types"

const CustomPosthogProvider: CustomPosthogProviderType = ({children}) => {
    const router = useRouter()
    const [loadingPosthog, setLoadingPosthog] = useState(false)
    const [posthogClient, setPosthogClient] = useAtom(posthogAtom)

    const initPosthog = useCallback(async () => {
        if (posthogClient) return
        if (loadingPosthog) return
        if (!getEnv("NEXT_PUBLIC_POSTHOG_API_KEY")) return

        setLoadingPosthog(true)

        try {
            const posthog = (await import("posthog-js")).default

            if (!getEnv("NEXT_PUBLIC_POSTHOG_API_KEY")) return

            posthog.init(getEnv("NEXT_PUBLIC_POSTHOG_API_KEY"), {
                api_host: "https://app.posthog.com",
                // Enable debug mode in development
                loaded: (posthog) => {
                    setPosthogClient(posthog)
                    if (process.env.NODE_ENV === "development") posthog.debug()
                },
                capture_pageview: false,
                ...((isDemo() ? CLOUD_CONFIG : OSS_CONFIG) as Partial<PostHogConfig>),
            })
        } finally {
            setLoadingPosthog(false)
        }
    }, [loadingPosthog, posthogClient, setPosthogClient])

    useEffect(() => {
        initPosthog()
    }, [initPosthog])

    const handleRouteChange = useCallback(() => {
        posthogClient?.capture("$pageview", {$current_url: window.location.href})
    }, [posthogClient])

    useEffect(() => {
        router.events.on("routeChangeComplete", handleRouteChange)

        return () => {
            router.events.off("routeChangeComplete", handleRouteChange)
        }
    }, [handleRouteChange, router.events])

    return <>{children}</>
}

const CustomPosthogProviderWrapper: CustomPosthogProviderType = ({children, config}) => {
    if (getEnv("NEXT_PUBLIC_POSTHOG_API_KEY")) {
        return <CustomPosthogProvider config={config}>{children}</CustomPosthogProvider>
    } else {
        return <>{children}</>
    }
}

export default CustomPosthogProviderWrapper
