# Desinstalador de Pacotes Python

Este pequeno script automatiza a desinstalação de pacotes Python listados em um arquivo `req.txt`.

## Como usar

1. Crie um arquivo `req.txt` contendo os pacotes que deseja desinstalar, um por linha:

```
numpy
pandas
scikit-learn
```

2. Execute o script:

```bash
python uninstall_packages.py
```

O script irá ler todos os pacotes listados no `req.txt` e desinstalá-los automaticamente.

## Observações

- Certifique-se de ter permissões adequadas para desinstalar pacotes do Python.
- O script usa `pip uninstall -y` para desinstalar sem pedir confirmação.