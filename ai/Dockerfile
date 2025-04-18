FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /workspace

# 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip vim git && \
    rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 대기 상태 유지 (VS Code attach를 위한 설정)
CMD ["tail", "-f", "/dev/null"]
