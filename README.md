Worm Propagation Visualization Project
Project Overview

In this project, you will create a controlled environment that visualizes how two "classic" computer worms propagate through a network. This will require implementing virtualization, networking, security controls, monitoring, and visualization components.
Learning Objectives

    Understand worm propagation mechanisms through practical implementation
    Design and implement secure network segmentation
    Apply proper containment controls for malicious code
    Develop monitoring tools for infection tracking
    Create effective visualizations of attack propagation
    Practice leveraging AI tools for complex technical tasks

Project Requirements
Core Deliverables

    Worm Selection and Research
        Select two classic computer worms with different propagation methods
        Document their infection vectors, propagation techniques, and payloads
        Propose specific containment measures based on propagation characteristics
    Virtualization Environment
        Script to set up VMs with the vulnerabilities needed for worm propagation
        Network configuration with segmentation (networks of no more than 5 VMs)
        Cross-network connections (some VMs must belong to multiple networks)
        Secure containment measures to prevent worm escape (REQUIRED)
    Monitoring and Visualization
        Tracking script to monitor infection status on each VM
        Visual representation of network topology with infection status indicators
        Visualization of depth-first search (DFS) algorithm over the network graph
        Dynamic visualization showing actual worm propagation in real-time
        Reset capability to restart the simulation

Technical Specifications

    Minimum of 15 VMs across at least 4 network segments
    Network must include VMs that bridge between segments
    Containment measures must allow egress traffic for worm propagation between VMs while preventing escape
    Visualization must clearly show:
        Network topology
        Current infection status (red/green node coloring)
        Propagation path as infection spreads

Project Phases and Checkpoints
Phase 1: Research and Planning (Checkpoint 1)

Deliverable: Research document containing:

    Selected worms with technical details and historical significance
    Propagation mechanisms and required vulnerabilities
    Proposed containment strategy specific to selected worms
    High-level architecture diagram of planned implementation
    Visualization approach and technologies

Instructor approval required before proceeding
Phase 2: Environment Setup (Checkpoint 2)

Deliverable: Working code and documentation for:

    VM provisioning scripts
    Network configuration
    Vulnerability implementation
    Containment measures

Demonstration of successful environment required
Phase 3: Monitoring Implementation (Checkpoint 3)

Deliverable: Working code and documentation for:

    Infection tracking scripts
    Data collection mechanism
    Initial visualization of network topology

Demonstration of monitoring capability required
Phase 4: Visualization and Final Implementation

Deliverable: Complete project including:

    Final visualization system
    DFS algorithm visualization
    Dynamic worm propagation visualization
    Reset functionality
    Comprehensive documentation
    Demonstration video

Resources for Worm Selection

When selecting your worms, consider researching these classic examples:

    Morris Worm (1988)
    Code Red (2001)
    Nimda (2001)
    SQL Slammer (2003)
    Blaster (2003)
    Sasser (2004)
    Conficker (2008)

Helpful resources for your research:

    The Malware Museum (Internet Archive)
    Academic papers on historical worms
    Security reports from the time periods
    CVE database entries for related vulnerabilities

Visualization Suggestions

You may choose any visualization approach that meets the requirements. Some suggestions include:

    Web-Based Dashboard
        JavaScript libraries like D3.js, Sigma.js, or CytoscapeJS
        Real-time updates via WebSockets
        Interactive node inspection
    Python-Based Solution
        NetworkX with Matplotlib or PyGraphviz
        Dash or Streamlit for interactive components
        Custom tkinter application
    Specialized Visualization Tools
        Gephi with custom data importers
        ELK stack (Elasticsearch, Logstash, Kibana)
        Grafana dashboards with appropriate data sources
    Custom Low-Level Implementation
        Processing or p5.js for visual programming
        Custom C++/SDL or Java application

Testing Procedures

Your implementation will be tested using the following procedures:
Containment Testing

    External Network Access Test
        A monitoring system will be attached to your environment's external network interface
        Alerts will be configured for any unexpected outbound connection attempts
        The worm simulation will be run for a full propagation cycle
        Any detected outbound traffic that could contain worm code will result in automatic failure
    VM Escape Test
        Access controls will be verified between the host system and virtualized environment
        VM configurations will be analyzed for improper network configurations
        Host system will be monitored for any signs of infection or unexpected behavior

Functionality Testing

    Propagation Accuracy Test
        Worm propagation will be manually traced and compared to visualization
        Timing of infections will be verified against expected propagation patterns
        Network constraints should appropriately limit or channel worm movement
    Visualization Accuracy Test
        Network topology visualization will be compared to actual network configuration
        Infection status indicators must accurately reflect VM state
        DFS visualization must correctly represent the algorithm's path through the network
    System Resilience Test
        Random VMs will be disabled during propagation to test visualization adaptability
        Reset functionality must completely clean all infections and return to initial state
        Multiple consecutive simulations must produce consistent results

Grading Criteria

Component	Weight	Description
Research Quality	15%	Depth of understanding of selected worms
Network Architecture	20%	Appropriate segmentation and complexity
Security Controls	20%	Effectiveness of containment (Automatic fail if inadequate)
Monitoring Implementation	15%	Accuracy and reliability of infection tracking
Visualization Quality	20%	Clarity, accuracy and informativeness
Documentation	10%	Completeness, clarity, and technical accuracy

AI Usage Guidelines

You are encouraged to leverage AI tools (such as Claude, ChatGPT, GitHub Copilot) to assist with this project. However:

    Document which aspects were developed with AI assistance
    Explain how you prompted the AI and refined its outputs
    Demonstrate understanding of all code in your implementation
    Be prepared to explain and modify any AI-generated components

Effective AI usage is considered a valuable skill, but you must demonstrate your own understanding and critical thinking throughout the project.
Final Submission Requirements

Your final submission must include:

    All source code with clear documentation
    Setup instructions for reproducing your environment
    Video demonstration of the working system
    Technical report documenting design decisions, challenges, and solutions
    Reflection on the project including AI usage assessment

Important Reminder

SECURITY NOTICE: This project involves creating an environment with intentional vulnerabilities. You MUST implement proper containment. Failure to do so will result in an automatic failing grade. Never deploy this environment on production networks or publicly accessible systems.

