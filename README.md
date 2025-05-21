### 1. Source code được chia thành các phần như sau
```
amr_robot/
├── amr_description/         # Mô hình robot (URDF, meshes)
├── amr_bringup/             # Launch tổng khởi chạy toàn hệ thống
├── amr_navigation/          # Điều hướng (Nav2, bản đồ, planner, controller)
├── amr_localization/        # Định vị (AMCL, EKF, map_server)
├── amr_slam/                # Tạo bản đồ (SLAM Toolbox hoặc Cartographer)
├── amr_driver/              # Driver phần cứng (Lidar, IMU, Motor)
├── amr_hardware/            # ros2_control và config phần cứng thực
├── amr_web_interface/       # Giao diện web quản lý robot (FastAPI + frontend)
├── amr_msgs/                # ROS2 message/service tùy chỉnh (nếu cần)
├── amr_maps/                # Thư viện bản đồ mở rộng (tuỳ chọn)
├── amr_tasks/               # Logic nhiệm vụ tự động (patrol, giao hàng...)
├── amr_simulation/          # Mô phỏng bằng Gazebo
├── amr_tests/               # Unit test & integration test
└── README.md                # Hướng dẫn tổng quan dự án
```