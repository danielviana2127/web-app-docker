#!/usr/bin/env bash
set -euo pipefail

URL="http://localhost:8000"
TIMEOUT=5

if ! command -v curl >/dev/null 2>&1; then
  echo "❌ curl não está instalado"
  exit 1
fi

echo "🔍 Testando aplicação em: $URL"

STATUS=$(curl --max-time "$TIMEOUT" -o /dev/null -s -w "%{http_code}" "$URL" || true)

if [ "$STATUS" != "200" ]; then
  echo "❌ Aplicação não respondeu corretamente"
  echo "Status HTTP recebido: $STATUS"
  exit 1
fi

echo "✅ Aplicação respondeu corretamente com HTTP 200"
