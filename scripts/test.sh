#!/bin/bash
set -e

URL="http://localhost:8000"

echo "Testando aplicação em $URL"

STATUS=$(curl -o /dev/null -s -w "%{http_code}" $URL)

if [ "$STATUS" -ne 200 ]; then
  echo "❌ Aplicação não respondeu corretamente (status $STATUS)"
  exit 1
fi

echo "✅ Aplicação respondeu com HTTP 200"

