# hng14-stage2-devops

This repository contains a microservices-based job processing system. It features a Node.js frontend, a FastAPI backend, a Python-based worker, and a Redis message queue.

## Prerequisites

  * **Docker** (version 20.10.0 or higher)
  * **Docker Compose** (version 2.0.0 or higher)
  * **Git**

## Setup Instructions

### 1\. Clone the Repository

```bash
git clone https://github.com/[YOUR_USERNAME]/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2\. Configure Environment Variables
 Create a `.env` file from the provided template:

```bash
cp .env.example .env
```

Open the `.env` file and ensure the `REDIS_PASSWORD` is set. **Do not commit this file to version control.**

### 3\. Build and Launch the Stack

Run the following command to build the images and start all services in the background:

```bash
docker compose up -d --build
```

## What a Successful Startup Looks Like

To verify the system is running correctly, perform the following checks:

### 1\. Check Container Status

Run `docker compose ps`. You should see four containers running. All should show a status of `(healthy)`:

| Name | Status | Port Mapping |
| :--- | :--- | :--- |
| **frontend** | Up (healthy) | 0.0.0.0:3000-\>3000/tcp |
| **api** | Up (healthy) | 0.0.0.0:8000-\>8000/tcp |
| **worker** | Up (healthy) | N/A (Internal) |
| **redis** | Up (healthy) | N/A (Internal) |

### 2\. Access the Dashboards

  * **Frontend UI**: Open [http://localhost:3000](https://www.google.com/search?q=http://localhost:3000) in your browser. You should see the "Job Processor Dashboard".
  * **API Docs**: Visit [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs) to view the Swagger UI.

### 3\. Verify the Workflow

1.  Click **"Submit New Job"** on the Frontend UI.
2.  The job status should immediately appear as `queued`.
3.  After approximately 2 seconds, the status should automatically update to `completed`.

## 🧹 Shutdown

To stop the services and clean up the internal network:

```bash
docker compose down
```

-----