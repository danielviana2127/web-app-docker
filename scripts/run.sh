#!/usr/bin/env bash
set -euo pipefail

COMPOSE_CMD="docker compose"
APP_URL="http://localhost:8000"
WAIT_TIME=10

echo "🚀 Subindo aplicação com Docker Compose..."
$COMPOSE_CMD up -d --build

echo "⏳ Aguardando aplicação iniciar..."
sleep $WAIT_TIME

echo "🔍 Verificando containers em execução..."
$COMPOSE_CMD ps

echo "✅ Aplicação disponível em:"
echo "$APP_URL"

echo "📌 Para acompanhar os logs:"
echo "$COMPOSE_CMD logs -f"