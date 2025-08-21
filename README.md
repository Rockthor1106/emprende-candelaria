![Logo de Emprende Candelaria](./docs/images/logo.jpg)
# Emprende Candelaria - Vitrina Digital

**Una plataforma diseñada para conectar a los emprendedores de Candelaria, Valle del Cauca, con sus clientes, impulsando la economía local a través de la tecnología.**

[Link al Demo del Frontend] · [Link a la Documentación de la API]

---

## 1. El Problema

En el municipio de Candelaria, muchos pequeños y medianos emprendimientos carecen de una presencia digital efectiva. Dependen de redes sociales desorganizadas o del "voz a voz", lo que limita su visibilidad y potencial de crecimiento. Los clientes, por su parte, no tienen un lugar centralizado para descubrir la rica y variada oferta comercial del municipio.

## 2. La Solución

**Emprende Candelaria** es una API RESTful que sirve como backend para una vitrina digital. La plataforma permite a los emprendedores registrarse de forma sencilla, crear un perfil atractivo para su negocio y gestionar un catálogo digital de sus productos. Esto proporciona un canal directo y organizado para que los clientes exploren, califiquen y contacten a los negocios locales.

## 3. Arquitectura del Sistema

Este proyecto está construido con una arquitectura desacoplada y serverless, pensada para ser altamente escalable y eficiente en costos, ideal para un producto que empieza a crecer.

- **Backend API:** Django REST Framework desplegado en **AWS Lambda** con API Gateway.
- **Base de Datos:** **Amazon Aurora Serverless** (compatible con PostgreSQL) para escalar automáticamente según la demanda.
- **Frontend:** (Desarrollado por separado) Aplicación de una sola página (SPA) construida con **React**.
- **Despliegue Frontend:** **Vercel**, para integración y despliegue continuo.

*(Sugerencia: Puedes crear un diagrama simple con una herramienta como draw.io y enlazar la imagen aquí)*

---

## 4. Características Principales (MVP)

La API cubre los siguientes requerimientos funcionales:

#### Módulo de Cuentas y Perfiles
- ✅ **(RF-01)** Registro de emprendedores basado en email con verificación.
- ✅ **(RF-02)** Gestión completa del perfil del negocio (logo, banner, contacto, etc.).
- ✅ **(RF-03)** Administración de usuarios desde el panel de Django Admin.

#### Módulo de Catálogo
- ✅ **(RF-04)** Gestión de categorías y productos por parte de cada negocio.
- ✅ **(RF-05)** Endpoint público para visualizar el perfil de un negocio y su catálogo completo.
- ✅ Gestión de múltiples fotos por producto.

#### Módulo de Interacción
- ✅ **(RF-06)** Sistema de reseñas y calificaciones públicas por parte de los visitantes.
- ✅ **(RF-07)** Cálculo y visualización de la calificación promedio por negocio.

---

## 5. Documentación de la API

La API está completamente documentada usando OpenAPI (Swagger). La documentación interactiva se puede consultar en el siguiente endpoint una vez que el proyecto está corriendo:

- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`

---
