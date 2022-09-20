# Serverless Dynamic Website

## Architecture
<p align="center">
  <img src="Slide.png" width="450" height="300" title="Architecture"> 
</p>

# Steps to replicate
* Setup S3 public bucket
	1. create a public bucket with below bucket policy
	```bash
	{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::charleskamalanandpublic/*"
        }
    ]
	}
	```
  

<!-- 1. item1
1. item2
    1. subitem1
    2. subitem2 -->

