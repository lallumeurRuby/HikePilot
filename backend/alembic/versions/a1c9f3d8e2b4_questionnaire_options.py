"""questionnaire options and scenarios

Revision ID: a1c9f3d8e2b4
Revises: bb06dbacc4a3
Create Date: 2026-09-18 16:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1c9f3d8e2b4'
down_revision: Union[str, None] = 'bb06dbacc4a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('questionnaire_question_option',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_code', sa.String(), nullable=False),
    sa.Column('option_code', sa.String(), nullable=False),
    sa.Column('option_text', sa.String(), nullable=False),
    sa.Column('display_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question_code', 'option_code')
    )
    op.create_table('questionnaire_question_scenario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_code', sa.String(), nullable=False),
    sa.Column('scenario_code', sa.String(), nullable=False),
    sa.Column('scenario_text', sa.String(), nullable=False),
    sa.Column('display_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question_code', 'scenario_code')
    )


def downgrade() -> None:
    op.drop_table('questionnaire_question_scenario')
    op.drop_table('questionnaire_question_option')
