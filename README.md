# Network-Aware-Placement-System-for-URLLC-service-in-Edge-cloud-environment


##Purpose and intention of the idea development

Edge computing technology has emerged to overcome the increase in communication volume caused by commercialization of 5G and IoT.
 However, not only is there a lack of suitable scheduling policies for next-generation networks, but no task assignment has been made to efficiently utilize edge computing.
  Therefore, in this project, we aim to develop a scheduler suitable for Kubernetes, a container orchestration system, to deploy URLLC (Ultra-Reliable Low Latency Communication) services in the edge cloud environment.
***
##Content and scope of idea development

In this task, we will deploy the scheduler, the basic component of Kubernetes, to the URLLC service, taking into account two factors of the network environment: round trip time (RTT) and bandwidth.
Accordingly, an application program for monitoring network information and an API-based service for performance verification were developed.
***
##Development results

In this project, we developed a cluster server-based virtual edge cloud, Koren SDI-based edge cloud, an API-based tool that can monitor network information, and a scheduler that can select the optimal network edge node. 
Among the developed results, the ***NAS*** and ***HRDF*** schedulers showed that the average delay rate was significantly reduced by more than 30% compared to the basic scheduling method.
***
##Benefit

The technology proposed in this project can be expected to meet the delay time required for VR/AR and autonomous driving, and it is easy to access the technology by solving the absence of a solution or system framework for edge cloud. Therefore, it is not only useful in enterprise 5G, Smart City, deployment environment, but also improves the performance of URLLC service.
Future Work introduces machine learning through channel estimation data to improve the selection in the node selection process of ***NAS***, and through Application Aware, the possibility of technological advancement can be expected by reducing time in the scheduling process.
*** 