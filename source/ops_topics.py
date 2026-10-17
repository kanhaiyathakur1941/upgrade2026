from helper import lesson, mod

OPS = [
    mod("linux-git", "Linux and Git", [
        lesson(
            "linux-fs",
            "Filesystem, permissions, users, processes, systemd",
            "beginner", "essential", 50,
            "You already SSH to Ubuntu. Name ls, chmod, chown, ps, top, journalctl, ss without guessing flags in the interview.",
            code='''# read-only investigation shape
# journalctl -u nginx -n 50 --no-pager
# ss -lptn
# tail -n 100 /var/log/nginx/access.log | grep ' 500 ' ''',
            refs=["[man pages via man7](https://man7.org/linux/man-pages/)"],
            nxt="#linux-net",
        ),
        lesson(
            "linux-net",
            "Networking, SSH, env, pipes, logs, curl",
            "beginner", "essential", 40,
            "curl -i shows headers. pipes and redirection are how you isolate a 500 without a GUI.",
            code='''# curl -i https://example.com
# ssh -i key.pem ubuntu@HOST
# export DATABASE_URL=postgres://...
# grep 500 /var/log/nginx/access.log | tail''',
            mistakes=["sshing as root for app work", "leaving 22 open to 0.0.0.0/0"],
            nxt="#git-flow",
        ),
        lesson(
            "git-flow",
            "Branch, commit, merge, rebase, PR, tags",
            "beginner", "essential", 40,
            "Small commits. Rebase only your unpublished branch. Never force-push shared main. Tags mark the v0.1.0 you ship on day 30.",
            how="feature branch → PR → tests → merge. Conflict: take the tenant filter from both sides if each added a different clause. Signed commits are optional.",
            mistakes=["git add . that includes .env", "rebase of a branch two people push"],
            nxt="#docker-core",
        ),
    ]),
    mod("ship", "Docker, CI, AWS, Nginx, later IaC", [
        lesson(
            "docker-core",
            "Images, containers, Dockerfile, Compose, security",
            "intermediate", "essential", 60,
            "Image is the recipe. Container is the process. Multi-stage builds drop compilers. Run as non-root. Secrets are env, not layers.",
            code='''# Dockerfile shape
# FROM python:3.12-slim AS base
# WORKDIR /app
# COPY pyproject.toml .
# RUN pip install --no-cache-dir .
# COPY src ./src
# USER nobody
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]''',
            refs=["[Docker](https://docs.docker.com/)"],
            nxt="#cicd-gha",
        ),
        lesson(
            "cicd-gha",
            "GitHub Actions: test, lint, image, rollback idea",
            "intermediate", "essential", 45,
            "PR runs pytest. Main builds an image. Staging then production. Rollback is a previous image, not a hope.",
            refs=["[GitHub Actions](https://docs.github.com/actions)"],
            nxt="#aws-core",
        ),
        lesson(
            "aws-core",
            "IAM, EC2, S3, RDS, VPC, SG, ALB, ASG, CloudWatch, SQS, SNS, Secrets",
            "intermediate", "essential", 70,
            "Speak EC2, S3, SNS, Nginx, Ubuntu, Docker, Jenkins as used. Treat VPC, ALB, IAM design, CloudWatch, ECS, SQS as study until you operate them.",
            how="IAM least privilege. Security group as stateful firewall: 443 public, SSH limited, DB private. CloudWatch is logs and alarms. SQS is the queue; SNS is fan-out.",
            refs=["[AWS](https://docs.aws.amazon.com/)"],
            nxt="#nginx-tls",
        ),
        lesson(
            "nginx-tls",
            "Nginx, TLS, app servers, process managers",
            "intermediate", "essential", 40,
            "Nginx terminates TLS and proxies to uvicorn or PHP-FPM. Workers are a second process, like queue:work.",
            nxt="#iac-tf",
        ),
        lesson(
            "iac-tf",
            "Terraform fundamentals",
            "advanced", "optional", 40,
            "After you can deploy by hand. State, providers, plan vs apply. Optional until a role asks.",
            refs=["[Terraform](https://developer.hashicorp.com/terraform/docs)"],
            nxt="#k8s-fund",
        ),
        lesson(
            "k8s-fund",
            "Kubernetes: what and when",
            "advanced", "optional", 40,
            "Learn after Docker Compose and one AWS deploy. Pods, services, deployments. Skip cluster admin for the 90-day target.",
            refs=["[Kubernetes](https://kubernetes.io/docs/)"],
            nxt="#sd-reqs",
        ),
    ]),
]
