resource "aws_s3_bucket" "dl" {
    bucket = "datalake-marco-xpe-edc1-tf"
    acl    = "private"


    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }


    tags = {
        IES   = "XPe"
        CURSO = "EDC"
    }


}