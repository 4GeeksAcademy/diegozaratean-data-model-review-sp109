from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Consola(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    precio: Mapped[int] = mapped_column(nullable=False)

    consolas_videojuegos = relationship("ConsolaVideojuego", back_populates="consola")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # do not serialize the password, its a security breach
        }
    
class Empresa(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    ciudad: Mapped[str] = mapped_column(nullable=False)
    slogan: Mapped[str] = mapped_column(nullable=False)

    videojuegos = relationship("Videojuego", back_populates="empresa")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # do not serialize the password, its a security breach
        }
    
class Videojuego(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)

    id_empresa = mapped_column(ForeignKey("empresa.id"))
    empresa = relationship("Empresa", back_populates="videojuego")

    consolas_videojuegos = relationship("ConsolaVideojuego", back_populates="videojuego")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # do not serialize the password, its a security breach
        }


class ConsolaVideojuego(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    id_consola = mapped_column(ForeignKey("consola.id"))
    consola = relationship("Consola", back_populates="consola_videojuego")

    id_videojuego = mapped_column(ForeignKey("videojuego.id"))
    videojuego = relationship("Videojuego", back_populates="consola_videojuego")
   

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }