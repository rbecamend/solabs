#!/bin/sh

echo "Iniciando o servidor Ollama..."
ollama serve &

# Espera 5 segundos antes de tentar o pull
sleep 8

echo "Tentando baixar o modelo llama3..."
ollama pull llama3.2:latest || echo "Erro"

echo "Pronto. Mantendo container ativo..."
tail -f /dev/null