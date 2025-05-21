### 1. Chi tiết hơn được mô tả ở dưới
```
amr_robot/
│
├── amr_description/             # (1) Định nghĩa mô hình robot (URDF, meshes)
│   ├── urdf/
│   │   └── amr_robot.urdf
│   ├── meshes/
│   │   └── *.stl
│   └── launch/
│       └── view_amr.launch.py
│
├── amr_bringup/                 # (2) Khởi chạy hệ thống robot (URDF + nav + loc + driver)
│   └── launch/
│       └── bringup.launch.py
│
├── amr_navigation/              # (3) Navigation2 (AMCL, Map Server, Planner, Controller)
│   ├── config/
│   │   └── nav2_params.yaml
│   ├── maps/
│   │   ├── maze.pgm
│   │   ├── maze.yaml
│   │   └── maze.data
│   └── launch/
│       └── navigation.launch.py
│
├── amr_localization/            # (4) Localization (AMCL, EKF)
│   ├── config/
│   │   ├── ekf.yaml
│   │   └── amcl.yaml
│   └── launch/
│       └── localization.launch.py
│
├── amr_slam/                    # (5) SLAM (slam_toolbox hoặc cartographer)
│   ├── config/
│   │   └── slam_params.yaml
│   ├── maps/                    # (Optional) nơi lưu tạm bản đồ mới tạo
│   │   └── new_map.pgm
│   └── launch/
│       └── slam_toolbox.launch.py
│
├── amr_driver/                  # (6) Driver phần cứng: Lidar, IMU, Motor
│   ├── lidar/
│   │   └── launch/lidar.launch.py
│   ├── imu/
│   └── motor/
│       └── launch/motor_driver.launch.py
│
├── amr_hardware/                # (7) Điều khiển phần cứng thực qua ros2_control
│   ├── config/
│   │   └── diff_drive_controller.yaml
│   └── launch/
│       └── hardware.launch.py
│
├── amr_web_interface/           # (8) Giao diện điều khiển qua web
│   ├── backend/                 # FastAPI hoặc Flask
│   │   └── main.py
│   ├── frontend/                # React / HTML + JS
│   │   └── index.html
│   └── mqtt_bridge/             # ROS ↔ MQTT/WebSocket
│       └── mqtt_node.py
│
├── amr_msgs/                    # (9) Message hoặc service tuỳ chỉnh (nếu cần)
│   └── msg/
│       └── RobotStatus.msg
│
├── amr_maps/                    # (10) Thư viện bản đồ mở rộng (tuỳ chọn)
│   ├── factory/
│   │   ├── factory.pgm
│   │   ├── factory.yaml
│   │   └── factory.data
│   └── warehouse/
│       └── ...
│
├── amr_tasks/                   # (11) Logic nhiệm vụ tự động: giao hàng, tuần tra,...
│   ├── path_planning/
│   └── behavior_tree/
│
├── amr_simulation/              # (12) Gazebo mô phỏng
│   ├── launch/
│   ├── world/
│   └── model/
│
├── amr_tests/                   # (13) Unit test, integration test
│
└── README.md                    # Tài liệu hướng dẫn sử dụng

```