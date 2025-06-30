
## Getting Started with the Unitree Z1 SDK

To start working with the Unitree Z1 SDK, follow these steps:

### 1. Make sure you have all dependencies installed before running these commands.

```bash
sudo apt update
sudo apt install libboost-dev libeigen3-dev
```

### 2. Clone and Build the Z1 Controller

First, clone the controller repository:

```bash
git clone https://github.com/unitreerobotics/z1_controller.git
cd z1_controller
mkdir build && cd build
cmake .. && make
```

---

### 3. Clone and Build the Z1 SDK

Navigate to the Z1 Controller folder and build it:

```bash
git clone https://github.com/unitreerobotics/z1_sdk.git
cd z1_sdk
mkdir build && cd build
cmake .. && make
```

### 4. Insert this repo in the z1_sdk folder

Navigate inside the z1_sdk folder and git clone this repo

```bash
cd z1_sdk
git clone https://github.com/notdana/unitree_z1_py_examples.git
```

---

After this, you should be ready to begin working with the Z1 SDK in your development environment.



# Fixing ImportError for `unitree_arm_interface`: Missing `libZ1_SDK_x86_64.so`

When running the python examples , you may encounter the following error:

```bash
Traceback (most recent call last):
  File "example_highcmd.py", line 3, in <module>
    import unitree_arm_interface
ImportError: libZ1_SDK_x86_64.so: cannot open shared object file: No such file or directory
```

This error means that Python found the `unitree_arm_interface` module, but couldn’t load its required shared library:

> `libZ1_SDK_x86_64.so: cannot open shared object file: No such file or directory`

This `.so` file is a **compiled C/C++ shared library**, and Python needs it at runtime to use the C++ extension behind `unitree_arm_interface`.


## How to Fix It

### Step 1: Locate the `.so` File

You need to find where `libZ1_SDK_x86_64.so` exists on your system. Run this command:

```bash
find ~/ -name "libZ1_SDK_x86_64.so" 2>/dev/null
```

Let’s say it’s located at (which mostly it is):

```
/home/yoursystem/unitree_z1_sdk/lib/libZ1_SDK_x86_64.so
```

---

### Step 2: Add Its Location to `LD_LIBRARY_PATH`

Now you need to tell your system where to find the shared object file:

```bash
export LD_LIBRARY_PATH=/home/danana/unitree_z1_sdk/lib:$LD_LIBRARY_PATH
```

After that, run your Python script **in the same terminal session**:

```bash
python3 example_highcmd.py
```

---

### Make It Permanent (Optional)

To avoid running the export command every time, add it to your shell configuration file:

- For bash:
  ```bash
  echo 'export LD_LIBRARY_PATH=/home/danana/unitree_z1_sdk/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
  source ~/.bashrc
  ```

- For zsh:
  ```bash
  echo 'export LD_LIBRARY_PATH=/home/danana/unitree_z1_sdk/lib:$LD_LIBRARY_PATH' >> ~/.zshrc
  source ~/.zshrc
  ```

---

### You're all set!

Once the environment variable is set correctly, Python will be able to find the `libZ1_SDK_x86_64.so` file and load the `unitree_arm_interface` module successfully.