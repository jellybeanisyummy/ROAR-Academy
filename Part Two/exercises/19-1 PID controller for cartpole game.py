import gym
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import warnings
warnings.filterwarnings('ignore')

# Exercise: Please adjust the Kp, Ki, and Kd to achieve the max 500 points
Kp = 3
Ki = 0
Kd = 3

errorList = []

def pid_controller(angle, angle_velocity, integral, prev_error, dt=0.02):
    error = angle
    integral += error * dt
    derivative = (error - prev_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    errorList.append(error)
    return control, integral, error

# Try different ways to create the environment
env = None
render_method = None

# Method 1: Try with old API
try:
    env = gym.make('CartPole-v1')
    env.reset()
    env.render(mode='rgb_array')
    render_method = 'old_rgb'
    print("Using old render API with rgb_array mode")
except:
    pass

# Method 2: Try default render
if env is None or render_method is None:
    try:
        env = gym.make('CartPole-v1')
        env.reset()
        env.render()
        render_method = 'old_default'
        print("Using old render API with default mode")
    except:
        pass

# Method 3: Just create environment without render
if env is None:
    env = gym.make('CartPole-v1')
    render_method = 'manual'
    print("Created environment, will attempt manual visualization")

# Test reset to check API version
state_or_tuple = env.reset()
if isinstance(state_or_tuple, tuple):
    state, _ = state_or_tuple
    uses_new_api = True
else:
    state = state_or_tuple
    uses_new_api = False

print(f"API version: {'new' if uses_new_api else 'old'}")

# Function to get frame based on render method
def get_frame(env, render_method):
    try:
        if render_method == 'old_rgb':
            return env.render(mode='rgb_array')
        elif render_method == 'old_default':
            # Try to get rgb_array even if not default
            try:
                return env.render(mode='rgb_array')
            except:
                return None
        else:
            return None
    except:
        return None

# Manual visualization fallback
def draw_cartpole_state(state, step, reward):
    """Manually draw the cartpole state"""
    cart_pos = state[0]
    pole_angle = state[2]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Set up the plot
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 2)
    ax.set_aspect('equal')
    
    # Draw track
    ax.plot([-2.4, 2.4], [0, 0], 'k-', linewidth=2)
    ax.plot([-2.4, -2.4], [-0.05, 0.05], 'r-', linewidth=4)
    ax.plot([2.4, 2.4], [-0.05, 0.05], 'r-', linewidth=4)
    
    # Draw cart
    cart_width = 0.3
    cart_height = 0.2
    cart = plt.Rectangle((cart_pos - cart_width/2, -cart_height/2), 
                        cart_width, cart_height, 
                        fill=True, color='blue')
    ax.add_patch(cart)
    
    # Draw pole
    pole_length = 1.0
    pole_end_x = cart_pos + pole_length * np.sin(pole_angle)
    pole_end_y = pole_length * np.cos(pole_angle)
    ax.plot([cart_pos, pole_end_x], [0, pole_end_y], 'brown', linewidth=8)
    
    # Add pole joint
    circle = plt.Circle((cart_pos, 0), 0.05, color='black')
    ax.add_patch(circle)
    
    # Add title
    ax.set_title(f'Step: {step}, Reward: {reward:.0f}, Angle: {np.degrees(pole_angle):.1f}°')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Position')
    ax.set_ylabel('Height')
    
    return fig

# Run one episode
angle = state[2]
angle_velocity = state[3]
integral = 0.0
prev_error = angle
total_reward = 0

print("\nRunning CartPole with PID Controller...")
print("Watch the game below:\n")

for t in range(500):
    # PID control
    control, integral, prev_error = pid_controller(angle, angle_velocity, integral, prev_error)
    action = 1 if control > 0 else 0
    
    # Step environment
    if uses_new_api:
        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
    else:
        state, reward, done, info = env.step(action)
    
    # Update state
    angle = state[2]
    angle_velocity = state[3]
    total_reward += reward
    
    # Display every 10 steps or when done
    if t % 10 == 0 or done:
        clear_output(wait=True)
        
        # Try to get frame
        frame = get_frame(env, render_method)
        
        if frame is not None:
            # Display captured frame
            plt.figure(figsize=(8, 6))
            plt.imshow(frame)
            plt.axis('off')
            plt.title(f'Step: {t+1}, Reward: {total_reward:.0f}')
            plt.show()
        else:
            # Use manual visualization
            fig = draw_cartpole_state(state, t+1, total_reward)
            plt.show()
            plt.close()
    
    if done:
        print(f"\nGame Over! Lasted {t + 1} steps with total reward: {total_reward}")
        
        # Show final state
        fig = draw_cartpole_state(state, t+1, total_reward)
        plt.show()
        plt.close()
        break
else:
    print(f"\nCompleted all 200 steps! Total reward: {total_reward}")

env.close()

# plot the error list
plt.figure(figsize=(12, 6))
plt.plot(errorList, linewidth=2, color='red')
plt.title('PID Controller Error (Pole Angle) Over Time', fontsize=14, weight='bold')
plt.xlabel('Time Steps')
plt.ylabel('Pole Angle Error (radians)')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linestyle='--', alpha=0.5, label='Target (0 radians)')
plt.legend()

# Show summary
print(f"\nPID Controller Performance:")
print(f"  Kp = {Kp} (Proportional)")
print(f"  Ki = {Ki} (Integral)")
print(f"  Kd = {Kd} (Derivative)")
print(f"  Steps survived: {t + 1}")
print(f"  Total reward: {total_reward}")