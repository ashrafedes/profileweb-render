from PIL import Image, ImageFilter
from pathlib import Path

SRC = Path('ERP_EVIDENCE')

def blur(im, box, r=14):
    region = im.crop(box).filter(ImageFilter.GaussianBlur(r))
    im.paste(region, box)
    return im

def done(im, name):
    im.save(SRC / name)
    print(name, im.size)

# 1. Analytics dashboard (1392x3072) - blur top-projects & top-subcontractor charts (client/sub names)
im = Image.open(SRC / 'raw_analytics_dashboard.png').convert('RGB')
blur(im, (70, 2240, 690, 2620))    # Top Projects by Value chart (project names)
blur(im, (735, 2240, 1360, 2620))  # Top Subcontractors by Value chart (sub names)
done(im, 'safe_01_analytics_dashboard.png')

# 2. Work Orders (1600x900) - blur project dropdown label + all data rows
im = Image.open(SRC / 'raw_work_orders.png').convert('RGB')
blur(im, (305, 45, 610, 75))       # selected project name in dropdown
blur(im, (95, 590, 1500, 835))     # data rows (subcontractor names, WO#, link codes, values)
done(im, 'safe_02_work_orders.png')

# 3. PM Daily Progress (1600x900) - blur WO/RITM id column in table rows
im = Image.open(SRC / 'raw_pm_daily_progress.png').convert('RGB')
blur(im, (245, 700, 390, 835))     # work order id column
done(im, 'safe_03_pm_daily_progress.png')

# 4. Permits tracking (1600x900) - blur permit numbers + coordination request numbers
im = Image.open(SRC / 'raw_permits_tracking.png').convert('RGB')
blur(im, (150, 350, 240, 780))     # permit no column
blur(im, (300, 350, 475, 780))     # coordination request number column
done(im, 'safe_04_permits_tracking.png')

# 5. Material flow (1600x900) - blur detail table rows (project + supplier names)
im = Image.open(SRC / 'raw_material_flow.png').convert('RGB')
blur(im, (95, 700, 1500, 870))     # material details table body
done(im, 'safe_05_material_flow.png')

# 6. Warehouse balance (1600x900) - blur supplier + project columns
im = Image.open(SRC / 'raw_warehouse_balance.png').convert('RGB')
blur(im, (760, 480, 910, 840))     # supplier column
blur(im, (1080, 480, 1270, 840))   # project column
done(im, 'safe_06_warehouse_balance.png')

print('done')
