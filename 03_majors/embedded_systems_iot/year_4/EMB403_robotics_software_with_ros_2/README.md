# EMB403 · Robotics Software with ROS 2

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [EMB303](../../year_3/EMB303_electronics_and_interfacing_for_programmers/README.md) (with [EMB302](../../year_3/EMB302_real_time_operating_systems/README.md), [EMB305](../../year_3/EMB305_embedded_linux/README.md), [FND113](../../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) and [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) assumed) | [EMB501](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md) |

## Why this course matters now

Warehouse robots, agricultural rovers, inspection drones, hospital delivery carts and research humanoids are mostly built on the same open software stack: ROS 2 for communication, Gazebo for simulation, Nav2 for navigation, MoveIt 2 for manipulation, and micro-ROS for the microcontrollers underneath. The stack has a predictable release rhythm: ROS 2 Jazzy Jalisco (May 2024, Ubuntu 24.04) is supported until May 2029 and pairs with Gazebo Harmonic (also supported to May 2029); Lyrical Luth was scheduled for May 2026 as the next long-term release, supported until May 2031, alongside Gazebo Jetty. Robot learning is moving fast too: open vision-language-action models such as NVIDIA's GR00T N1.7 and Physical Intelligence's π0.5, and the Hugging Face LeRobot library with low-cost SO-100 arms, put learned manipulation within reach of a student lab. AI assistants write ROS nodes and launch files well, but they often mix ROS 1 and ROS 2 APIs, use the wrong quality-of-service settings for sensor data, or get coordinate frames backwards, and a robot that turns left when the map says right is a physical hazard. This course teaches you to build, simulate, debug and deploy a complete mobile robot stack, and to know what each layer is doing.

## Learning outcomes

By the end you can:

1. **Design** a robot software architecture (drivers, perception, state estimation, planning, control) and **decide** which parts run on a microcontroller, on Linux, or in the cloud.
2. **Build** ROS 2 systems in C++ and Python with topics, services, actions, parameters, lifecycle nodes, components and launch files.
3. **Configure and debug** middleware: DDS and Zenoh-based RMWs, quality-of-service profiles, discovery on real networks, and latency tracing.
4. **Model** a robot with URDF/xacro and **maintain** a correct tf2 frame tree following REP 105.
5. **Write** sensor drivers and **integrate** lidar, IMU, encoders and cameras with correct timestamps and calibration.
6. **Control** hardware with ros2_control and micro-ROS, including odometry and PID tuning.
7. **Simulate** robots in Gazebo and **run** simulation tests in CI, and **measure** the sim-to-real gap.
8. **Estimate** state with EKF sensor fusion and **build** maps with SLAM, then **navigate** autonomously with Nav2 and tune it.
9. **Plan** arm motions with MoveIt 2 and **evaluate** a learned manipulation policy with LeRobot.
10. **Deploy** robot software safely: containers, cross-builds, emergency stops, speed limits, logging with rosbag2.

## Chapters and lessons

### Chapter 1 · Robot software architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Sense, plan, act | Layers of a mobile robot stack; where latency and determinism matter | Draw the architecture of a warehouse robot and a lawn mower |
| 1.2 What ROS 2 is | Middleware plus tools plus packages; why ROS 2 replaced ROS 1 (DDS, real-time friendliness, security) | Install ROS 2 Jazzy on Ubuntu 24.04 or in Docker; run the turtlesim and demo nodes |
| 1.3 Distributions and support | LTS vs non-LTS releases (Humble, Jazzy, Kilted, Lyrical), matching Gazebo versions, upgrade planning | Choose a distribution for a 5-year product and justify it |
| 1.4 MCU, Linux, cloud | micro-ROS on microcontrollers, Linux compute boards, fleet services | Assign 12 robot functions to the right compute tier |

**Check your understanding:** Why should motor current control not run in a ROS node on Linux? What do you gain and lose by picking a non-LTS distribution? Why is ROS called middleware rather than an operating system?

### Chapter 2 · ROS 2 core concepts (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Nodes and topics | Publishers, subscribers, message types, `ros2` CLI introspection | Write a C++ talker and a Python listener with a custom message |
| 2.2 Quality of service | Reliability, durability, history depth, deadline, liveliness; sensor-data vs default profiles | Create a QoS mismatch that silently drops messages; diagnose with `ros2 topic info -v` |
| 2.3 Executors and callback groups | Single- and multi-threaded executors, mutually exclusive vs reentrant groups, blocking callbacks | Show a deadlocked service call inside a callback; fix it with callback groups |
| 2.4 Parameters and launch | Declared parameters, YAML files, Python launch files, namespaces and remapping | Launch two robots in different namespaces from one file |

**Check your understanding:** Why does a "reliable" subscriber not receive from a "best effort" publisher? What happens when a callback blocks a single-threaded executor? Why namespace everything?

### Chapter 3 · Services, actions and lifecycle (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Services | Request/response, asynchronous clients, timeouts | Build a service that resets odometry; call it from code and CLI |
| 3.2 Actions | Goals, feedback, results, cancellation; when to use each communication type | Write a "drive to distance" action server with cancellation |
| 3.3 Lifecycle nodes | Managed states (unconfigured, inactive, active), orchestrated start-up | Convert a driver to a lifecycle node; start a system in order |
| 3.4 Composition | Components, intra-process communication, zero-copy for large messages | Compose camera and processing nodes; measure the latency saved |

**Check your understanding:** Why is navigation an action rather than a service? What problem do lifecycle nodes solve at start-up? When does composition matter for performance?

### Chapter 4 · Middleware, networks and tracing (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The RMW layer | DDS implementations (Fast DDS, Cyclone DDS), Zenoh-based middleware, discovery | Run the same system with two RMWs; compare discovery time and CPU |
| 4.2 Real networks | Domain IDs, multicast over Wi-Fi, discovery servers, large messages over wireless | Make a robot-to-laptop link work reliably over campus Wi-Fi |
| 4.3 Measuring latency | `ros2_tracing`, end-to-end latency, timestamps in headers | Trace a sensor-to-command pipeline; find the slowest hop |
| 4.4 Security | SROS2: authentication, encryption and access control for topics | Enable SROS2 for two nodes; show an unauthorised node is refused |

**Check your understanding:** Why does DDS discovery struggle on some Wi-Fi networks? Where would you look first if a topic's latency jumps from 5 ms to 200 ms? What does SROS2 protect, and what does it not?

### Chapter 5 · Frames, transforms and robot models (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Coordinate frames | `map`, `odom`, `base_link`, sensor frames; REP 105 conventions; right-hand rule | Draw the frame tree of a differential-drive robot with lidar and camera |
| 5.2 tf2 | Static and dynamic transforms, lookups at a time, extrapolation errors | Transform a lidar point into the map frame by hand and with tf2; compare |
| 5.3 URDF and xacro | Links, joints, inertia, collision vs visual geometry, `robot_state_publisher` | Model your robot in xacro; visualise in RViz2 |
| 5.4 Time | Clocks, simulation time, timestamp correctness and its effect on fusion | Inject a 100 ms timestamp error and show the effect on a map |

**Check your understanding:** Why are `map` and `odom` separate frames? What does a "transform extrapolation into the future" error tell you? Why must collision geometry be simpler than visual geometry?

### Chapter 6 · Sensors and drivers (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Lidar and range sensors | `LaserScan` and point clouds, range noise, minimum range, reflective surfaces | Bring up a 2D lidar and characterise its noise on a wall |
| 6.2 IMUs and encoders | Gyro bias and drift, accelerometer noise, encoder resolution and slip | Log an IMU for 10 minutes; estimate gyro bias drift |
| 6.3 Cameras and depth | `image_transport`, compressed transport, camera intrinsics calibration, depth cameras | Calibrate a camera; measure reprojection error |
| 6.4 Writing a driver node | Serial or I2C device to ROS messages, correct frame IDs and timestamps, diagnostics | Write a ROS 2 driver for your EMB303 sensor board |

**Check your understanding:** Why should a driver stamp messages with acquisition time rather than publish time? What fools a 2D lidar in a typical Indian office or home (glass, black surfaces)? Why calibrate even an expensive camera?

### Chapter 7 · Hardware interfaces and control (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Motor control on a microcontroller | PWM, encoders, PID speed loops at fixed rates (from EMB302/EMB303) | Tune a wheel speed PID; plot step responses |
| 7.2 micro-ROS | micro-ROS on FreeRTOS or Zephyr (ESP32 or Pico), the agent, transports | Publish encoder ticks and subscribe to wheel commands from an MCU |
| 7.3 ros2_control | Hardware interfaces, controller manager, `diff_drive_controller`, joint state broadcaster | Drive your robot through ros2_control with keyboard teleoperation |
| 7.4 Odometry | Wheel odometry, calibration of wheel radius and track width, drift | Calibrate odometry with a square path test; report error |

**Check your understanding:** Why put the speed loop on the microcontroller and the path follower on Linux? What does a wrong track width do to odometry? How do you know your PID is tuned well enough?

### Chapter 8 · Simulation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Gazebo with ROS 2 | SDF worlds, `ros_gz` bridges, sensor plugins, Gazebo Harmonic with Jazzy | Spawn your URDF robot in a simulated office |
| 8.2 Simulating sensors honestly | Noise models, update rates, physics step size | Match simulated lidar noise to your Chapter 6 measurements |
| 8.3 Tests in simulation | `launch_testing`, headless simulation in CI, scenario tests | Write a CI test that fails if the robot hits a wall |
| 8.4 Sim-to-real gaps | Friction, latency, lighting, sensor artefacts; GPU simulators such as NVIDIA Isaac Sim (awareness) | Run the same scenario in simulation and reality; list the 5 biggest differences |

**Check your understanding:** Why can a controller that works perfectly in simulation oscillate on the real robot? What makes a simulation test trustworthy in CI? When is a GPU simulator worth its cost?

### Chapter 9 · State estimation (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Uncertainty | Covariance, process vs measurement noise, why odometry drifts | Plot odometry drift over a 5-minute drive |
| 9.2 Kalman filters | Predict and update, the extended Kalman filter, tuning covariances | Implement a 1D Kalman filter by hand; then a 2D EKF in Python |
| 9.3 Sensor fusion with robot_localization | Fusing wheel odometry and IMU; frames and configuration | Fuse odometry and IMU; compare heading error with odometry alone |
| 9.4 Particle filters | Monte Carlo localisation (AMCL) on a known map | Localise in a known map from an unknown start; report convergence time |

**Check your understanding:** Why does fusing a gyro improve heading but not position drift from wheel slip? What happens when you set measurement noise too low? Why can AMCL fail in symmetric corridors?

### Chapter 10 · SLAM (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Occupancy grids | Log-odds updates, resolution trade-offs | Build a grid map from logged scans with known poses |
| 10.2 Scan matching and graph SLAM | Pose graphs, loop closure, optimisation; slam_toolbox | Map a building floor with slam_toolbox; save and reload the map |
| 10.3 Evaluating maps | Loop-closure errors, comparing against a floor plan, repeatability | Map the same area 3 times; measure differences |
| 10.4 Visual and 3D SLAM | Feature-based visual SLAM (ORB-SLAM3), RTAB-Map, when 3D is needed | Run a visual SLAM demo on a recorded dataset |

**Check your understanding:** Why does a map "bend" without loop closure? What causes false loop closures, and what do they do to the map? When is a 2D lidar map not enough?

### Chapter 11 · Navigation with Nav2 (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Costmaps | Static, obstacle and inflation layers, footprint, resolution | Tune inflation so the robot passes through a doorway but not too close to walls |
| 11.2 Planners and controllers | Global planners (NavFn, Smac), local controllers (DWB, Regulated Pure Pursuit, MPPI) | Compare two controllers on the same course: time, smoothness, clearance |
| 11.3 Behaviour trees | Navigation behaviour trees, recoveries, custom nodes | Add a custom recovery that backs up and rotates |
| 11.4 Tuning and failure analysis | Oscillation, getting stuck, dynamic obstacles, localisation loss | Diagnose 4 recorded navigation failures from rosbags |

**Check your understanding:** Why does a robot oscillate in front of a narrow gap? What should happen when localisation confidence collapses? Why use behaviour trees rather than a state machine?

### Chapter 12 · Manipulation, learning and deployment (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 MoveIt 2 | Planning scene, inverse kinematics, motion planning, collision checking | Plan pick-and-place for a simulated arm |
| 12.2 Learned manipulation | Imitation learning and VLA policies with LeRobot (ACT, Diffusion Policy, SmolVLA, π0.5); data collection by teleoperation | Train or fine-tune a small policy on a recorded dataset; evaluate success rate |
| 12.3 Recording and replay | rosbag2 (MCAP), replaying for regression tests, Foxglove for visualisation | Turn a field failure into a replayable regression test |
| 12.4 Deployment | Docker images, cross-building for ARM, boot-time start-up, logging, remote access | Deploy your stack as containers to the robot computer |
| 12.5 Safety basics | Emergency stops in hardware, speed and force limits, watchdogs on command streams, safe testing practice | Prove the robot stops within a set distance when commands stop |

**Check your understanding:** Why must an emergency stop not depend on ROS? How would you measure whether a learned policy is good enough to deploy? What makes a rosbag a better bug report than a video?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Install and introspect | Architecture diagram |
| 2 | 2 | Lab 2 · QoS and executors | — |
| 3 | 3 | Lab 3 · Actions and lifecycle | — |
| 4 | 4 | Lab 4 · Middleware and tracing | **P1 due** |
| 5 | 5 | Lab 5 · URDF and tf2 | — |
| 6 | 6 | Lab 6 · A driver node, and an AI audit | — |
| 7 | 7 | Lab 7 · micro-ROS and ros2_control | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Simulation tests in CI | — |
| 9 | 9 | Lab 9 · EKF fusion | — |
| 10 | 10 | Lab 10 · SLAM a floor | **P2 due** |
| 11 | 11 | Nav2 tuning (in P3) | — |
| 12 | 12 | MoveIt 2 and LeRobot | — |
| 13 | 12 | Deployment and safety tests (in P3) | — |
| 14 | — | — | **P3 due** |
| 15 | Review | Live demonstration and oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** boilerplate nodes, message definitions, launch files and URDF/xacro scaffolding; Nav2 parameter explanations; plotting scripts for rosbag data; converting between Python and C++ nodes; summarising papers on SLAM or robot learning before you read them.
- **Do without AI (drills):** drawing a frame tree and composing two transforms by hand; Kalman filter predict/update steps on paper; choosing QoS for 6 data streams; diagnosing a navigation failure from a rosbag. The mid-term and final are AI-off.
- **Verify AI output by:** building with `colcon` and running `ros2 doctor`; checking the graph with `rqt_graph` and the frame tree with `tf2_tools view_frames`; confirming QoS with `ros2 topic info -v`; running a simulation test before any real-robot test; checking that every package and API exists for your distribution.
- **Where AI still fails here (show it yourself):** in Lab 6 you ask an assistant for a driver node and a launch file, then build and run them. Log the defects. Typical ones: ROS 1 APIs (`rospy`, `roslaunch` XML) presented as ROS 2, launch syntax from an older distribution, Gazebo Classic plugins and `ign` commands instead of current `gz` tools, reliable QoS on high-rate sensor topics, frame IDs that break REP 105, and timestamps set at publish time. On real hardware, every assistant-written motion command is first run in simulation and then with the robot on blocks (wheels off the ground).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 live demonstration | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) given a broken ROS 2 system (QoS mismatch, wrong frame, blocked executor), find and fix all faults in 45 minutes using only ROS tools; (2) explain your robot's frame tree and EKF configuration and predict what happens if one sensor's covariance is wrong; (3) show your P3 robot completing an autonomous navigation course in a mapped space with a measured success rate and a hardware emergency stop that works independently of software.

## Industry reality

Where this is used: warehouse and logistics robots, agricultural robots, inspection and security robots, hospital delivery robots, research platforms and increasingly humanoids. ROS 2's long-term-support releases and the matching Gazebo LTS releases (Harmonic to May 2029, Jetty to May 2031) set the planning horizon for many robot products (ROS REP 2000 and Gazebo release pages). Robot learning toolkits have become open and accessible: LeRobot (Apache 2.0) supports imitation-learning and VLA policies, including π0, π0.5, SmolVLA and GR00T N1.7, and low-cost arms such as the SO-100. Robotics roles typically combine embedded skills (drivers, real-time control) with probabilistic estimation and Linux systems work (analysis).

**Interview questions from this course**

1. *When do you use a topic, a service or an action in ROS 2?* Strong answer: topics for streams, services for short request/response, actions for long-running goals with feedback and cancellation; examples of each; mentions QoS for topics and why services should not block executors.
2. *Explain the `map`, `odom` and `base_link` frames.* Strong answer: REP 105; `odom` is continuous but drifts, `map` is globally consistent but can jump; who publishes each transform (odometry/EKF vs localisation/SLAM); why the split keeps controllers smooth.
3. *Your subscriber receives nothing even though the topic exists. How do you debug it?* Strong answer: check QoS compatibility (`ros2 topic info -v`), message type, namespaces and remapping, domain IDs, network discovery, executor blocked, then tracing.
4. *How would you fuse wheel odometry and an IMU?* Strong answer: EKF with a motion model, which states each sensor contributes (IMU for yaw rate, odometry for velocity), covariance tuning, frames and timestamps, testing with ground truth or a square path.
5. *The robot keeps getting stuck in doorways with Nav2. What do you check?* Strong answer: footprint and inflation radius versus door width, costmap resolution, controller choice and parameters, localisation quality near the door, recovery behaviours; uses rosbags to reproduce and tests in simulation.

## Resources (free first)

- **Documentation:** ROS 2 Jazzy documentation — https://docs.ros.org/en/jazzy/ ; REP 2000 (distributions and target platforms) — https://www.ros.org/reps/rep-2000.html ; REP 105 (coordinate frames for mobile platforms) — https://www.ros.org/reps/rep-0105.html ; Nav2 — https://docs.nav2.org/ ; Gazebo — https://gazebosim.org/docs/ ; ros2_control — https://control.ros.org/ ; MoveIt 2 — https://moveit.picknik.ai/ ; micro-ROS — https://micro.ros.org/
- **Packages:** slam_toolbox — https://github.com/SteveMacenski/slam_toolbox ; robot_localization — https://github.com/cra-ros-pkg/robot_localization ; ros2_tracing — https://github.com/ros2/ros2_tracing ; LeRobot — https://github.com/huggingface/lerobot ; Foxglove — https://foxglove.dev/
- **Texts and courses (free):** Kevin Lynch and Frank Park, *Modern Robotics* (free PDF and videos) — http://hades.mech.northwestern.edu/index.php/Modern_Robotics ; Russ Tedrake, *Underactuated Robotics* (MIT, free) — https://underactuated.mit.edu/ ; Articulated Robotics ROS 2 tutorials — https://articulatedrobotics.xyz/ ; Duckietown (open robotics education platform) — https://duckietown.com/
- **Papers for Chapter 12:** Zhao et al., ACT / "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" (arXiv 2304.13705) — https://arxiv.org/abs/2304.13705 ; Chi et al., "Diffusion Policy" (arXiv 2303.04137) — https://arxiv.org/abs/2303.04137 ; Shukor et al., "SmolVLA" (arXiv 2506.01844) — https://arxiv.org/abs/2506.01844
- **Paid, optional:** Thrun, Burgard and Fox, *Probabilistic Robotics* (MIT Press), the standard estimation and SLAM text; Francisco Martín Rico, *A Concise Introduction to Robot Programming with ROS2* (CRC Press, 2022).

## Sources

- ROS REP 2000 source (Humble May 2022–May 2027; Jazzy May 2024–May 2029 with Gazebo Harmonic on Ubuntu 24.04; Kilted May 2025–Nov 2026) — https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-2000.rst (checked 2026-10)
- ROS 2 documentation, Lyrical Luth release timeline (GA planned 22 May 2026; EOL May 2031; Ubuntu 26.04) — https://docs.ros.org/en/lyrical/Releases/lyrical/release-timeline.html (seen via search, 2026-10; the site blocked automated reading)
- Gazebo releases (Harmonic Sep 2023–May 2029 LTS; Jetty Sep 2025–May 2031 LTS) — https://gazebosim.org/docs/latest/releases/ (checked 2026-10)
- LeRobot repository (supported policies and arms; Apache 2.0) — https://github.com/huggingface/lerobot (checked 2026-10)
- NVIDIA Isaac-GR00T (N1.7, 3B parameters) — https://github.com/NVIDIA/Isaac-GR00T ; Physical Intelligence openpi (π0, π0-FAST, π0.5) — https://github.com/Physical-Intelligence/openpi (checked 2026-10)

_Last reviewed: 2026-10_
