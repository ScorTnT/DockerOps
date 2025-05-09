FROM node:18-alpine

WORKDIR /app

# package.json과 lock 파일만 먼저 복사
COPY package*.json ./

# 의존성 설치
RUN npm install

# 전체 소스 복사
COPY . .

# 개발 서버
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]