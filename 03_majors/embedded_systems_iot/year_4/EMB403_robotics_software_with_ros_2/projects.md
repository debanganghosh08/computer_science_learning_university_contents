# EMB403 · Labs and projects

Platform options: (A) build a low-cost differential-drive robot: a Raspberry Pi 4/5 running ROS 2 Jazzy, an ESP32 or Pico 2 running micro-ROS for motor control, two geared DC motors with encoders, a motor driver, an IMU and a low-cost 2D lidar; (B) use a lab robot of the TurtleBot class; (C) work in Gazebo for P1 and the labs, and share a lab robot for P2 and P3. Real-robot rules: speed limited to 0.5 m/s in shared spaces, a hardware emergency stop that cuts motor power, the robot on blocks (wheels off the ground) for first tests of any new motion code, and supervised operation near people.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Install and introspect | Install Jazzy (native or Docker); explore nodes, topics, services and parameters with the CLI and rqt | Architecture diagram for your robot; CLI transcript | 3 h |
| 2 · QoS and executors | Reproduce a QoS mismatch and a blocked executor; fix both | Diagnosis notes with `ros2 topic info -v` output; fixed code | 4 h |
| 3 · Actions and lifecycle | A cancellable "drive distance" action; a lifecycle driver started in order by a launch file | Code, launch file, a log of start-up transitions | 4 h |
| 4 · Middleware and tracing | Compare two RMWs; trace a sensor-to-command pipeline with `ros2_tracing` | Discovery time and CPU comparison; latency breakdown per hop | 4 h |
| 5 · URDF and tf2 | Model your robot in xacro; verify the frame tree; transform a point by hand and with tf2 | URDF, `view_frames` output, the hand calculation | 4 h |
| 6 · A driver node, and an AI audit | ROS 2 driver for your EMB303 sensor board with correct stamps and frames; audit an AI-written driver and launch file | Driver passing tests; audit table (ROS 1 APIs, wrong QoS, wrong frames, publish-time stamps) | 5 h |
| 7 · micro-ROS and ros2_control | Wheel speed PID on the MCU via micro-ROS; drive through `diff_drive_controller` | Step-response plots; teleoperation video; loop-timing jitter | 6 h |
| 8 · Simulation tests in CI | Spawn your robot in Gazebo Harmonic; a `launch_testing` scenario that fails on collision, run headless in CI | CI run link or log; the scenario code | 4 h |
| 9 · EKF fusion | Fuse wheel odometry and IMU with robot_localization; compare against a measured square path | Configuration, error table with and without fusion | 4 h |
| 10 · SLAM a floor | Map a floor with slam_toolbox three times; evaluate repeatability | Maps, rosbags, a repeatability measurement | 4 h |

## Projects

### P1 · A simulated robot with a custom action (L1, ~6 hours)

**Real-world inspiration.** Robot teams prototype behaviours in simulation before touching hardware, and expose motions as actions so that higher-level planners can start, monitor and cancel them.

**What to build.** A differential-drive robot in Gazebo with a URDF/xacro model, keyboard teleoperation, and a C++ action server `drive_distance` (with feedback and cancellation) implemented as a lifecycle node, all started from one launch file.

**Acceptance criteria**
- Driving 1.0 m in simulation ends within ±2 cm of the target in 10 of 10 runs.
- Cancelling a goal stops the robot within 200 ms (measured from the cancel request to zero commanded velocity).
- QoS choices for every topic are documented and justified.
- One command launches the whole system; the lifecycle node transitions are logged.
- A `ros2_tracing` capture shows the command pipeline latency.

**Stretch goals.** Add a rotate-to-angle action using IMU feedback; compose the nodes for intra-process communication and compare latency.

**What it proves to an employer.** You understand ROS 2's communication model well enough to build clean, controllable robot behaviours.

### P2 · A real robot base: control, odometry, fusion and mapping (L2, ~15 hours)

**Real-world inspiration.** Hospital delivery carts and warehouse robots depend on a well-calibrated base: a stable speed loop, accurate odometry, fused heading and a good map are prerequisites for everything above them (illustrative scenario).

**What to build.** On a real robot: wheel speed control on the microcontroller with micro-ROS, `diff_drive_controller` through ros2_control, calibrated wheel odometry, EKF fusion with the IMU, and a map of a real floor with slam_toolbox, with rosbags of every run.

**Acceptance criteria**
- Speed loop runs at 100 Hz or faster on the MCU, with measured period jitter reported.
- After calibration, a 2 m × 2 m square path returns within 5% of the path length (40 cm) of the start, averaged over 5 runs in each direction; the calibration method is documented.
- EKF fusion reduces heading error on the square test compared with odometry alone; both numbers reported.
- A map of at least 100 m² with at least one loop closure; across 3 mapping runs, the positions of 5 chosen wall corners agree within 10 cm.
- Rosbags (MCAP) of each run and a README to replay them.

**Stretch goals.** Add a camera and run visual SLAM on the same route; compare map quality and CPU load.

**What it proves to an employer.** You can bring up a real robot base properly, from motor loops to maps, and measure each layer.

### P3 · An autonomous indoor delivery robot (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Indoor delivery robots in hospitals, hotels and offices carry items between fixed stations, share corridors with people and must stop safely when something goes wrong (illustrative scenario).

**What to build.** A complete delivery system on your P2 robot: Nav2 with tuned costmaps and controller; a behaviour-tree mission (go to pickup, wait for a confirmation button or message, go to drop-off, return to dock) with custom recoveries; dynamic-obstacle handling; a hardware emergency stop independent of software; a command-stream watchdog on the microcontroller; containerised deployment that starts on boot; simulation scenario tests in CI; and regression tests built from recorded field failures.

**Acceptance criteria**
- **Reliability:** 20 delivery missions across 3 stations in a mapped space, with at least 18 completed without human intervention; mean mission time and path length reported.
- **People and obstacles:** when a person steps into the path at walking distance, the robot stops or re-plans without contact in 10 of 10 trials; no contact with any obstacle in all runs.
- **Emergency stop:** with the software deliberately hung, the hardware stop still cuts motor power (demonstrated on video).
- **Watchdog:** when velocity commands stop arriving, the microcontroller stops the motors within 500 ms in 10 of 10 trials.
- **Engineering:** CI runs at least 3 simulation scenarios on every push; at least 2 regression tests come from real failures you recorded; every failed field run has a short report with its rosbag.
- **Deployment:** after power-on, the robot is ready for missions within 2 minutes with no manual commands.

**Stretch goals.** Add a small arm and a pick-and-place step with MoveIt 2, or evaluate a learned LeRobot policy for the pick; coordinate two robots sharing a corridor; publish fleet status to your EMB304 backend.

**What it proves to an employer.** You can deliver a robot that does a job repeatedly and stops safely, with the testing discipline real robotics teams expect.

## Feeds into

- [EMB501 Frontier Seminar: Autonomous Systems and Physical AI](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md): P3 becomes the platform for learned policies, safety cases and research.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): many robotics theses start from a working navigation stack.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): a robotics variant of the flagship can reuse this stack.
