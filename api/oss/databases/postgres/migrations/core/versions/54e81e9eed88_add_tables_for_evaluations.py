"""add tables for evaluations

Revision ID: 54e81e9eed88
Revises: 9698355c7650
Create Date: 2025-04-24 07:27:45.801481

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "54e81e9eed88"
down_revision: Union[str, None] = "9698355c7650"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table(
        "evaluation_aggregated_results",
        "auto_evaluation_aggregated_results",
    )
    op.rename_table(
        "evaluation_evaluator_configs",
        "auto_evaluation_evaluator_configs",
    )
    op.rename_table(
        "evaluation_scenario_results",
        "auto_evaluation_scenario_results",
    )
    op.rename_table(
        "evaluation_scenarios",
        "auto_evaluation_scenarios",
    )
    op.rename_table(
        "evaluations",
        "auto_evaluations",
    )

    op.create_table(
        "evaluation_runs",
        sa.Column(
            "project_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "deleted_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "created_by_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "updated_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "deleted_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "name",
            sa.String(),
            nullable=True,
        ),
        sa.Column(
            "description",
            sa.String(),
            nullable=True,
        ),
        sa.Column(
            "meta",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "flags",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "data",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.VARCHAR,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "project_id",
            "id",
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE",
        ),
        sa.Index(
            "ix_evaluation_runs_project_id",
            "project_id",
        ),
    )

    op.create_table(
        "evaluation_scenarios",
        sa.Column(
            "project_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "deleted_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "created_by_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "updated_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "deleted_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "meta",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "flags",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.VARCHAR,
            nullable=False,
        ),
        sa.Column(
            "run_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "project_id",
            "id",
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "run_id"],
            ["evaluation_runs.project_id", "evaluation_runs.id"],
            ondelete="CASCADE",
        ),
        sa.Index(
            "ix_evaluation_scenarios_project_id",
            "project_id",
        ),
        sa.Index(
            "ix_evaluation_scenarios_run_id",
            "run_id",
        ),
    )

    op.create_table(
        "evaluation_steps",
        sa.Column(
            "project_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "deleted_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "created_by_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "updated_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "deleted_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "meta",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "flags",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.VARCHAR,
            nullable=False,
        ),
        sa.Column(
            "timestamp",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "key",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "repeat_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "retry_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "hash_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "trace_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "testcase_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "error",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "scenario_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "run_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "project_id",
            "id",
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "run_id"],
            ["evaluation_runs.project_id", "evaluation_runs.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "scenario_id"],
            ["evaluation_scenarios.project_id", "evaluation_scenarios.id"],
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint(
            "project_id",
            "run_id",
            "scenario_id",
            "key",
            "retry_id",
            "retry_id",
        ),
        sa.Index(
            "ix_evaluation_steps_project_id",
            "project_id",
        ),
        sa.Index(
            "ix_evaluation_steps_scenario_id",
            "scenario_id",
        ),
        sa.Index(
            "ix_evaluation_steps_run_id",
            "run_id",
        ),
    )

    op.create_table(
        "evaluation_metrics",
        sa.Column(
            "project_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "deleted_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
        ),
        sa.Column(
            "created_by_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "updated_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "deleted_by_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "meta",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "flags",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "data",
            postgresql.JSONB(none_as_null=True),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.VARCHAR,
            nullable=False,
        ),
        sa.Column(
            "scenario_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "run_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "project_id",
            "id",
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "run_id"],
            ["evaluation_runs.project_id", "evaluation_runs.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "scenario_id"],
            ["evaluation_scenarios.project_id", "evaluation_scenarios.id"],
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint(
            "project_id",
            "run_id",
            "scenario_id",
        ),
        sa.Index(
            "ix_evaluation_metrics_project_id",
            "project_id",
        ),
        sa.Index(
            "ix_evaluation_metrics_run_id",
            "run_id",
        ),
        sa.Index(
            "ix_evaluation_metrics_scenario_id",
            "scenario_id",
        ),
    )


def downgrade() -> None:
    op.drop_table("evaluation_metrics")
    op.drop_table("evaluation_steps")
    op.drop_table("evaluation_scenarios")
    op.drop_table("evaluation_runs")

    op.rename_table(
        "auto_evaluations",
        "evaluations",
    )
    op.rename_table(
        "auto_evaluation_scenarios",
        "evaluation_scenarios",
    )
    op.rename_table(
        "auto_evaluation_scenario_results",
        "evaluation_scenario_results",
    )
    op.rename_table(
        "auto_evaluation_evaluator_configs",
        "evaluation_evaluator_configs",
    )
    op.rename_table(
        "auto_evaluation_aggregated_results",
        "evaluation_aggregated_results",
    )
