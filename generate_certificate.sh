#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "사용법: $0 <IP 대역> <시작 번호> <끝 번호>"
    echo "예시: $0 192.168.219 100 107"
    exit 1
fi

ip_base=$1
start_num=$2
end_num=$3
cn="EDDI"

subjectAltName="subjectAltName ="
for ((i=start_num; i<=end_num; i++)); do
  if [ $i -eq $start_num ]; then
    subjectAltName+=" IP:$ip_base.$i"
  else
    subjectAltName+=", IP:$ip_base.$i"
  fi
done

echo "CA 개인 키 생성 중..."
openssl genpkey -algorithm RSA -out CA.key

echo "CA 인증서 생성 중..."
openssl req -x509 -new -nodes -key CA.key -sha256 -days 3650 -out CA.pem -subj "/C=KR/ST=Seoul/L=Seoul/O=My Organization/OU=My Unit/CN=$cn"

echo "서버 개인 키 생성 중..."
openssl genpkey -algorithm RSA -out svr.key

echo "서버 CSR 생성 중..."
openssl req -new -key svr.key -out svr.csr -subj "/C=KR/ST=Seoul/L=Seoul/O=My Organization/OU=IT Department/CN=$cn"

echo "서버 인증서 서명 중..."
openssl x509 -req -in svr.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out svr.crt -days 365 -sha256 -extfile <(echo "$subjectAltName")

echo "클라이언트 개인 키 생성 중..."
openssl genpkey -algorithm RSA -out client.key

echo "클라이언트 CSR 생성 중..."
openssl req -new -key client.key -out client.csr -subj "/C=KR/ST=Seoul/L=Seoul/O=My Organization/OU=IT Department/CN=$cn"

echo "클라이언트 인증서 서명 중..."
openssl x509 -req -in client.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out client.crt -days 365 -sha256 -extfile <(echo "$subjectAltName")

echo "모든 과정이 완료되었습니다."
