from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, ForeignKey, create_engine, select


class Base(DeclarativeBase):
    pass


class Game(Base):

    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    developer_id: Mapped[int] = mapped_column(Integer, ForeignKey('developer.id'))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    graphics_engine_id: Mapped[int] = mapped_column(Integer, ForeignKey('graphics_engine.id'))

    def __repr__(self) -> str:
        return f"Game(id={self.id!r}, title={self.title!r}, price={self.price!r}, developer={self.developer_id!r}, graphics_engine={self.graphics_engine_id!r})"


class Developer(Base):

    __tablename__ = "developer"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=True)

    def __repr__(self) -> str:
        return f"Developer(id={self.id!r}, name={self.name!r}, address={self.address!r})"


class GraphicsEngine(Base):

    __tablename__ = "graphics_engine"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    language: Mapped[str] = mapped_column(String(40), nullable=True)

    def __repr__(self) -> str:
        return f"Developer(id={self.id!r}, name={self.name!r}, language={self.language!r})"