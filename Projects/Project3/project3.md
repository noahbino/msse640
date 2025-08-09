# Project 3: Performance Testing

## MSSE640 - Software Quality and Test

### Table of Contents 

- [Introduction](#introduction)
- [Part 1: Performance Testing Research](#part-1-research-on-performance-testing-and-jmeter)
- [Part 2: Testing Documents](#part-2-test-document-with-screenshots)
- [Conclusion & Recommendations](#conclusion--recommendations)

### Introduction 

This project focuses on performance testing using Apache JMeter to evaluate the responsiveness, stability, and scalability of a web application. The target system for this test is my personal website, noahiarrobino.com, a single-page application. Through simulating multiple user requests under different load scenarios—Endurance, Load, and Stress/Spike tests, this project measures how the site performs over time, under varying traffic levels, and in sudden traffic surges. The goal is to identify performance bottlenecks and ensure the site can handle real-world usage efficiently.


### Part 1: Research on Performance Testing and JMeter

#### 1. Types of Performance Tests

##### Load Testing

Load testing evaluates how a system performs under expected user trafic, it determines response times, throughput , and resource usage when a known number of users access the system asynchronously. 

Graph (Time vs Threads)

Threads ^
   50 |          ───────────────
      |
      |
    0 +------------------------> Time


##### Endurance Testing 

Endurance testing checks the stability of the system under sustained load over a longer period. It helps detects memory leaks (retainment cycles in iOS), resource exhaustion, and slow degradation of performance. The goal is verify long term stability under a consistent workload. 

Threads ^
   20 |────────────────────────
      |
      |
    0 +------------------------> Time


##### Stress Testing

Stress testing pushes the system beyond its normal load limits to find its breaking point. While spike testing rapidly increases the number of users to test reaction to sudden surges traffic. The goal is to identify maximum capacity and how the system recovers from failures.

Threads ^
  200 |        /‾‾‾‾‾‾‾‾
      |       /
      |      /
   20 |─────
      |
    0 +------------------------> Time

### 2. JMeter Components 

###### Thread Groups

Thread Groups define the number of virtual users, the ramp-up period (how quickly users are added), and the test duration. Each thread represents one simulated user performing the test scenario.

###### HTTP Request Sampler

The HTTP Request Sampler sends HTTP or HTTPS requests to a web server. You can configure:
	•	Server Name or IP: noahiarrobino.com
	•	Protocol: https
	•	Path: / (homepage) or /api/... for API endpoints.

###### Config Elements

Config Elements provide reusable settings across samplers. Examples:
	•	HTTP Header Manager for setting Content-Type: application/json.
	•	User Defined Variables for base URLs and parameters.

###### Listeners

Listeners collect and display test results. Common listeners:
	•	View Results Tree – Detailed request/response logs.
	•	Summary Report – Metrics like average response time, throughput, and error %.
	•	Graph Results – Visual representation of performance over time.


#### 3. Application Performance Index 

The Application Performance Index (Apdex) is a standard method to measure user satisfaction with application response time.

Apdex = (Satisfied Count + (Tolerating Count / 2)) / Total Samples

	•	Satisfied: Responses faster than a set threshold T.
	•	Tolerating: Slower than T but faster than 4T.
	•	Frustrated: Slower than 4T.

Example:
If your threshold T is 0.5 seconds, and in 100 requests:
	•	70 were satisfied (< 0.5s)
	•	20 were tolerating (0.5s–2s)
	•	10 were frustrated (> 2s)

Apdex = (70 + (20 / 2)) / 100
Apdex = (70 + 10) / 100 = 0.80

This means your users are 80% satisfied with the site’s performance.


### Part 2: Test Document with Screenshots 

#### Endurance Test

![Endurance Test Setup](/Assets/enduranceTest.png)
![Endurance Test Results](/Assets/enduranceTestResults.png)

#### Load Test 

![Load Test Setup](/Assets/loadTest.png)
![Load Test Results](/Assets/loadTestResults.png)

#### Stress Test 

![Stress Test Setup](/Assets/stressTest.png)
![Stress Test Results](/Assets/stressTestResults.png)

### Conclusion & Recommendations 

Performance testing on my website (noahiarrobino.com) using JMeter provided insight into how the site responds under different load conditions. The tests confirmed that the site remains stable during endurance and moderate load scenarios but could be further optimized for sudden spikes in traffic.

It is recommended to implement caching for static resources, use a CDN to reduce latency, and monitor server performance during peak usage. Regular performance testing should be scheduled to ensure the site continues to meet performance expectations as traffic grows.