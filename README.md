# Horras Backend: Backend of Horras, the Haikou Online Ride-hailing Records Analysis System

This is the backend of Horras, the Haikou Online Ride-hailing Records Analysis System. It is a Fastapi project with a PostgreSQL database.
See the frontend project [here](https://github.com/yanglinshu/horras).

## Dependencies
Horras Backend is built on top of the following dependencies:
- [Fastapi](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Prisma](https://www.prisma.io/)
- [Docker](https://www.docker.com/)

## Installation
Horras Backend runs its database in a Docker container. To install the database, run the following command:
```bash
docker-compose up -d
```

To install the backend, run the following commands:
```bash
pip install -r requirements.txt

prisma db push

uvicorn horras_backend.main:app --host 0.0.0.0
```

For compatibility reasons, running the backend in a Docker container is not recommended.

## Usage
The backend is a Fastapi project. To access the API documentation, go to `http://localhost:8000/docs`.

## License
This repository is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
