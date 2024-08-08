// import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
// import { fromCognitoIdentityPool } from "@aws-sdk/credential-providers";
// import { S3Client } from "@aws-sdk/client-s3";
// import env from "@/env";

// const REGION = env.s3.AWS_REGION as string; // 리전 설정
// const IDENTITY_POOL_ID = env.s3.AWS_S3_IDENTITY_POOL_ID as string; // Identity Pool ID

// console.log('REGION:', REGION); // 디버깅을 위해 추가
// console.log('IDENTITY_POOL_ID:', IDENTITY_POOL_ID); // 디버깅을 위해 추가

// if (!REGION || !IDENTITY_POOL_ID) {
//     throw new Error("Missing required environment variables for AWS configuration");
// }

// const s3Client = new S3Client({
//     region: REGION,
//     credentials: fromCognitoIdentityPool({
//         identityPoolId: IDENTITY_POOL_ID,
//         clientConfig: { region: REGION },
//     }),
// });

// export { s3Client, env };
