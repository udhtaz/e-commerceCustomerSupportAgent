from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys

# --- Add  app path to the system path for imports ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Import the SQLAlchemy Base and models ---
from app.infrastructure.db.base import Base
from app.infrastructure.db.models import order

# this is the Alembic Config object, which provides access to the values within alembic.ini
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set the target metadata for 'autogenerate'
target_metadata = Base.metadata

# Database URL (optional: override from .env or set it statically here)
# Could also be pulled from settings module if needed
config.set_main_option(
    "sqlalchemy.url", f"sqlite:///{os.path.abspath('data/orders.db')}"
)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Entry point for migration execution
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
