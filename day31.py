import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (60, 60, 60)
BROWN = (101, 67, 33)
SNOW_WHITE = (240, 248, 255)
GOLD = (255, 215, 0)
LIGHT_GOLD = (255, 235, 100)
SKY_BLUE = (135, 206, 235)

def rotate_point_y(x, z, angle):
    """Rotate a point around the Y axis"""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    new_x = x * cos_a - z * sin_a
    new_z = x * sin_a + z * cos_a
    return new_x, new_z

def create_mountain():
    """Create the 3D points for Mount Fuji"""
    points = []
    
    # Mountain body - a cone shape with more detail
    layers = 30
    for layer in range(layers):
        height = layer / layers
        radius = (layers - layer) / layers * 150
        num_points = max(int(radius * 0.4), 8)
        
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            y = -100 + height * 200  # Mount goes from y=-100 to y=100
            points.append((x, y, z, 'mountain'))
    
    # Snow cap at the top
    snow_layers = 8
    for layer in range(snow_layers):
        height = 1.0 - (layer / snow_layers) * 0.4
        radius = (snow_layers - layer) / snow_layers * 40
        num_points = max(int(radius * 0.4), 8)
        
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            y = 70 + layer * 5
            points.append((x, y, z, 'snow'))
    
    return points

def create_halo():
    """Create the halo as a ring of points"""
    points = []
    radius = 80
    num_points = 100
    
    # Multiple rings for thickness
    for ring in range(3):
        r = radius + ring * 3
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            x = r * math.cos(angle)
            z = r * math.sin(angle)
            y = 150  # Position above the mountain
            points.append((x, y, z, 'halo'))
    
    # Inner glow
    inner_radius = 70
    for i in range(80):
        angle = (i / 80) * 2 * math.pi
        x = inner_radius * math.cos(angle)
        z = inner_radius * math.sin(angle)
        y = 150
        points.append((x, y, z, 'halo_glow'))
    
    # Add some sparkle points
    for i in range(20):
        angle = (i / 20) * 2 * math.pi
        for offset in [-5, 0, 5]:
            x = (radius + offset) * math.cos(angle)
            z = (radius + offset) * math.sin(angle)
            y = 150
            points.append((x, y, z, 'sparkle'))
    
    return points

def project_3d_to_2d(x, y, z):
    """Project 3D point to 2D screen coordinates with perspective"""
    # Perspective projection
    fov = 400
    distance = 500
    
    factor = fov / (distance + z)
    screen_x = int(x * factor + SCREEN_WIDTH / 2)
    screen_y = int(-y * factor + SCREEN_HEIGHT / 2)
    
    return screen_x, screen_y, z

def main():
    """Main animation loop"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mount Fuji with Halo")
    clock = pygame.time.Clock()
    
    angle = 0
    rotation_speed = 0.02
    
    # Get mountain and halo points (create once)
    mountain_points = create_mountain()
    halo_points = create_halo()
    all_points = mountain_points + halo_points
    
    # Font for text
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear screen with gradient sky
        for y in range(SCREEN_HEIGHT):
            color_value = int(135 + (y / SCREEN_HEIGHT) * 100)
            color = (min(color_value, 255), min(color_value + 50, 255), 235)
            pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))
        
        # Rotate and project points
        projected = []
        for x, y, z, point_type in all_points:
            # Rotate around Y axis
            rotated_x, rotated_z = rotate_point_y(x, z, angle)
            
            # Project to 2D
            screen_x, screen_y, depth = project_3d_to_2d(rotated_x, y, rotated_z)
            
            if 0 <= screen_x < SCREEN_WIDTH and 0 <= screen_y < SCREEN_HEIGHT:
                projected.append((screen_x, screen_y, depth, point_type))
        
        # Sort by depth (far to near for painter's algorithm)
        projected.sort(key=lambda p: -p[2])
        
        # Draw points
        for screen_x, screen_y, depth, point_type in projected:
            if point_type == 'mountain':
                # Shade based on depth
                shade = max(0, min(255, int(255 - (depth + 200) * 0.3)))
                color = (shade // 2, shade // 3, shade // 4)
                pygame.draw.circle(screen, color, (screen_x, screen_y), 3)
            elif point_type == 'snow':
                pygame.draw.circle(screen, SNOW_WHITE, (screen_x, screen_y), 3)
            elif point_type == 'halo':
                # Pulsing effect
                pulse = math.sin(pygame.time.get_ticks() * 0.003) * 20 + 235
                color = (255, int(pulse), 0)
                pygame.draw.circle(screen, color, (screen_x, screen_y), 4)
            elif point_type == 'halo_glow':
                alpha_surface = pygame.Surface((10, 10), pygame.SRCALPHA)
                pygame.draw.circle(alpha_surface, (255, 235, 100, 150), (5, 5), 5)
                screen.blit(alpha_surface, (screen_x - 5, screen_y - 5))
            elif point_type == 'sparkle':
                # Twinkling sparkles
                if (pygame.time.get_ticks() // 200) % 2 == 0:
                    pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 2)
        
        # Draw title
        title = font.render("MOUNT FUJI", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 30))
        # Shadow
        shadow = font.render("MOUNT FUJI", True, DARK_GRAY)
        screen.blit(shadow, (title_rect.x + 2, title_rect.y + 2))
        screen.blit(title, title_rect)
        
        # Draw angle info
        angle_text = small_font.render(f"Rotation: {math.degrees(angle) % 360:.1f}°", True, WHITE)
        screen.blit(angle_text, (10, SCREEN_HEIGHT - 30))
        
        # Update angle
        angle += rotation_speed
        if angle > 2 * math.pi:
            angle -= 2 * math.pi
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()