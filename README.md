### Hexlet tests and linter status:
[![Actions Status](https://github.com/kabanovic/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kabanovic/qa-auto-engineer-python-project-241/actions)

### GitHub Actions
[![Python CI](https://github.com/kabanovic/qa-auto-engineer-python-project-241/actions/workflows/pytests.yml/badge.svg)](https://github.com/kabanovic/qa-auto-engineer-python-project-241/actions/workflows/pytests.yml)

### Sonar
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=kabanovic_qa-auto-engineer-python-project-241&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=kabanovic_qa-auto-engineer-python-project-241)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=kabanovic_qa-auto-engineer-python-project-241&metric=bugs)](https://sonarcloud.io/summary/new_code?id=kabanovic_qa-auto-engineer-python-project-241)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=kabanovic_qa-auto-engineer-python-project-241&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=kabanovic_qa-auto-engineer-python-project-241)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=kabanovic_qa-auto-engineer-python-project-241&metric=coverage)](https://sonarcloud.io/summary/new_code?id=kabanovic_qa-auto-engineer-python-project-241)

## Установка и запуск

Для установки всех зависимостей выполните:

```bash
make install
```

### Использование

Утилита `gendiff` поддерживает три формата вывода (`stylish`, `plain`, `json`) и умеет сравнивать как `.json`, так и `.yaml` / `.yml` файлы.

**1. Формат по умолчанию (stylish):**
```bash
uv run gendiff path/to/file1.json path/to/file2.json
```

**2. Плоский текстовый формат (plain):**
```bash
uv run gendiff --format plain path/to/file1.yml path/to/file2.yaml
```

**3. Структурированный формат (json):**
```bash
uv run gendiff --format json path/to/file1.json path/to/file2.yaml
```

### Справка
```bash
uv run gendiff -h
```

### Generate_diff with default format
[![asciicast](https://asciinema.org/a/TOzDjUmMhG0xmwzl.svg)](https://asciinema.org/a/TOzDjUmMhG0xmwzl)

### Generate_diff with plian format
[![asciicast](https://asciinema.org/a/YnH8RI7R7E6lwXrH.svg)](https://asciinema.org/a/YnH8RI7R7E6lwXrH)

### Generate_diff with json format
[![asciicast](https://asciinema.org/a/iFEBy2QKBLh2sBhI.svg)](https://asciinema.org/a/iFEBy2QKBLh2sBhI)