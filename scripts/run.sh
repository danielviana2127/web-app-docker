#!/bin/bash
set -e

echo "Subindo aplicação com Docker Compose..."
docker compose up -d

echo "Aguardando aplicação iniciar..."
sleep 5

echo "Aplicação disponível em:"
echo "http://localhost:8000"

