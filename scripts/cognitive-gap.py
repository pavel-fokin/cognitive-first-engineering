import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Data
x = np.linspace(0, 10, 500)
# Human limit is low and flat
y_human_val = 3
y_human = np.full_like(x, y_human_val)
# Complexity starts near human limit and grows exponentially
y_complexity = np.exp(x * 0.4) + y_human_val - 1

# 2. Figure Setup (LinkedIn Portrait 4:5 - 1080x1350)
fig, ax = plt.subplots(figsize=(10.8, 13.5), dpi=100)
bg_color = '#F8F6F2'
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# 3. Plotting
# Style similar to inspiration: Dark Red for complexity, Grey/Blue for human
c_complexity = '#2c3e50'
c_human = '#2F4F4F'      # Dark Slate Grey
c_gap ='#e74c3c' 
c_gap_text = '#2F4F4F'

# Plot Lines
ax.plot(x, y_complexity, color=c_complexity, linewidth=4, zorder=10)
ax.plot(x, y_human, color=c_human, linewidth=4, zorder=10)

# Fill the Gap
# Using a pattern/hatch if possible, or just a clean color
mask = y_complexity > y_human
ax.fill_between(x, y_complexity, y_human, where=mask, 
                interpolate=True, color=c_gap, alpha=0.2, zorder=1)

# 4. Labels & Text (Smaller, following inspiration)

# Axis labels removed for infographic style

# Headline for thumb-stop value on LinkedIn
ax.text(5, 58, "The Cognitive Gap",
        fontsize=32, fontweight='bold', color=c_gap_text, ha='center', va='top')

# Line Labels (at the ends/following curve)
# Complexity Label
ax.text(8.5, 35, "System & AI\nComplexity", 
        fontsize=20, color=c_complexity, fontweight='bold', ha='right', va='bottom')

# Human Label
ax.text(6, 1, "Human Cognitive Limits",
        fontsize=20, color=c_human, fontweight='bold', ha='left', va='bottom')

# Gap Title - Central in the gap
gap_x = 7.9
gap_y = (np.exp(gap_x * 0.38) + y_human_val) / 2
ax.text(8, 13, "THE COGNITIVE GAP",
        fontsize=20, fontweight='bold', color=c_gap_text, ha='center', va='center')


# 5. Axis Formatting (Infographic Style)
ax.set_axis_off()

# Limits
ax.set_ylim(0, 60)
ax.set_xlim(0, 10)

# Remove ticks/labels on axes numbers
ax.set_xticks([])
ax.set_yticks([])

# 6. Save
output_path = "cognitive_gap.png"
plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.96])
plt.savefig(output_path, dpi=100)
print(f"Saved diagram-style plot to {output_path}")
