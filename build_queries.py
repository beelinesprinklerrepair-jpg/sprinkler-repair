import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# All raw data - (query, clicks, impressions, ctr%, position)
raw = [
    ("beeline sprinkler repair",92,261,35.25,1.19),
    ("sprinkler repair nampa",17,305,5.57,3.98),
    ("sprinkler repair near me",7,283,2.47,8.12),
    ("sprinkler repair meridian",7,103,6.80,8.93),
    ("sprinkler repair",6,131,4.58,8.27),
    ("sprinkler repair boise",4,157,2.55,7.23),
    ("nampa sprinkler repair",3,56,5.36,3.21),
    ("sprinkler repair nampa idaho",3,42,7.14,9.55),
    ("sprinkler installation near me",3,36,8.33,5.56),
    ("sprinkler repair caldwell",2,68,2.94,4.44),
    ("sprinkler service near me",2,37,5.41,6.97),
    ("boise sprinkler repair",2,36,5.56,9.47),
    ("sprinkler system",2,32,6.25,2.09),
    ("residential sprinkler repair near me",2,14,14.29,4.93),
    ("sprinkler maintenance companies near me",2,5,40.00,3.4),
    ("irrigation repair near me",1,65,1.54,9.18),
    ("beeline sprinkler repair reviews",1,56,1.79,2.91),
    ("irrigation repair",1,50,2.00,10.3),
    ("sprinkler repair meridian idaho",1,47,2.13,9.64),
    ("idaho sprinkler repair",1,38,2.63,8.58),
    ("irrigation system repair",1,33,3.03,11.7),
    ("sprinkler repair eagle idaho",1,24,4.17,16.04),
    ("lawn sprinkler repair",1,21,4.76,6.48),
    ("sprinkler repair caldwell idaho",1,14,7.14,6.21),
    ("sprinkler repair service",1,11,9.09,1.36),
    ("rain bird sprinkler system repair near me",1,7,14.29,4.71),
    ("sprinkler service",1,6,16.67,3.17),
    ("sprinkler maintenance near me",1,6,16.67,3.67),
    ("sprinkler companies near me",1,5,20.00,4.8),
    ("sprinkler repair service near me",1,3,33.33,1.0),
    ("irrigation repair companies near me",1,3,33.33,3.0),
    ("sprinkler irrigation companies near me",1,3,33.33,3.67),
    ("sprinkler repair near me free estimate",1,3,33.33,4.33),
    ("sprinkler repair company",1,3,33.33,15.67),
    ("sprinkler guy near me",1,2,50.00,5.0),
    ("repair sprinkler system",1,1,100.00,1.0),
    ("sprinkler business near me",1,1,100.00,1.0),
    ("sprinkler install",1,1,100.00,1.0),
    ("sprinkler system pump replacement",1,1,100.00,1.0),
    ("top rated irrigation repair near me",1,1,100.00,1.0),
    ("best sprinkler companies near me",1,1,100.00,2.0),
    ("sprinkler system installation cost",1,1,100.00,6.0),
    ("irrigation companies near me",1,1,100.00,18.0),
    ("sprinkler system repair",0,91,0.0,7.26),
    ("sprinkler blowout nampa",0,89,0.0,9.37),
    ("drip irrigation installation boise",0,77,0.0,1.0),
    ("treasure valley irrigation specialists",0,65,0.0,22.83),
    ("irrigation system repair meridian",0,52,0.0,27.83),
    ("sprinkler blowout meridian",0,48,0.0,28.12),
    ("lawn sprinkler repair boise id",0,44,0.0,19.36),
    ("sprinkler system installation treasure valley id",0,40,0.0,23.1),
    ("sprinkler blowout near me",0,39,0.0,9.51),
    ("sprinkler systems installation nampa",0,31,0.0,3.03),
    ("sprinkler system repair near me",0,31,0.0,16.0),
    ("sprinklers",0,30,0.0,1.6),
    ("sprinkler system repair meridian",0,30,0.0,31.87),
    ("sprinkler repair boise idaho",0,29,0.0,11.48),
    ("irrigation repair meridian",0,29,0.0,22.52),
    ("sprinkler",0,28,0.0,2.5),
    ("sprinkler systems installation star idaho",0,28,0.0,13.96),
    ("irrigation systems nampa",0,27,0.0,1.59),
    ("beeline",0,26,0.0,5.5),
    ("sprinkler system service",0,26,0.0,10.85),
    ("nampa sprinkler blowout",0,26,0.0,15.92),
    ("sprinkler blowout boise",0,26,0.0,40.5),
    ("sprinkler systems installation caldwell",0,25,0.0,13.36),
    ("sprinkler system service near me",0,23,0.0,18.96),
    ("sprinkler systems installation middleton",0,20,0.0,9.4),
    ("sprinkler company near me",0,18,0.0,6.0),
    ("sprinkler head replacement",0,18,0.0,6.22),
    ("irrigation repair eagle",0,18,0.0,14.61),
    ("irrigation pump repair",0,18,0.0,17.56),
    ("sprinkler blowouts meridian",0,18,0.0,39.72),
    ("sprinklers near me",0,17,0.0,4.76),
    ("sprinkler heads",0,17,0.0,6.18),
    ("irrigation systems middleton",0,16,0.0,9.31),
    ("lawn sprinkler repair meridian id",0,16,0.0,38.81),
    ("sprinkler blowouts nampa",0,13,0.0,4.31),
    ("irrigation system repair near me",0,13,0.0,10.08),
    ("sprinkler blowout caldwell",0,13,0.0,15.38),
    ("emergency sprinkler repair",0,12,0.0,10.5),
    ("sprinkler repair eagle",0,12,0.0,16.33),
    ("sprinkler winterization near me",0,12,0.0,20.83),
    ("water sprinkler system boise id",0,12,0.0,26.58),
    ("sprinkler installation boise",0,12,0.0,27.92),
    ("sprinkler blowouts",0,11,0.0,1.18),
    ("boise sprinkler installation",0,11,0.0,9.55),
    ("irrigation systems star idaho",0,11,0.0,17.36),
    ("sprinkler companies around me",0,11,0.0,21.27),
    ("sprinkler installation boise idaho",0,11,0.0,24.91),
    ("sprinkler line repair",0,10,0.0,2.8),
    ("irrigation installation nampa",0,12,0.0,1.0),
    ("sprinkler blowout nampa idaho",0,12,0.0,8.67),
    ("sprinkler valve replacement",0,9,0.0,6.11),
    ("sprinkler valves",0,9,0.0,6.89),
    ("sprinkler head",0,9,0.0,7.33),
    ("drip irrigation system",0,9,0.0,8.22),
    ("sprinkler and irrigation installation meridian",0,9,0.0,9.56),
    ("boise sprinkler system repair",0,9,0.0,14.11),
    ("irrigation systems eagle idaho",0,9,0.0,18.11),
    ("sprinkler blowout meridian idaho",0,9,0.0,29.44),
    ("lawn sprinkler system",0,8,0.0,1.12),
    ("sprinkler repair in nampa idaho",0,8,0.0,7.12),
    ("irrigation services",0,8,0.0,8.5),
    ("boise sprinkler",0,8,0.0,12.12),
    ("sprinkler blowout eagle",0,8,0.0,17.5),
    ("sprinkler blowout meridian id",0,8,0.0,42.88),
    ("meridian sprinkler blowout",0,8,0.0,44.0),
    ("irrigation system installation",0,7,0.0,1.0),
    ("sprinkler start up services",0,7,0.0,8.71),
    ("sprinkler service boise",0,7,0.0,10.14),
    ("sprinkler turn on near me",0,7,0.0,12.14),
    ("sprinkler and irrigation installation boise",0,7,0.0,13.0),
    ("meridian sprinkler repair",0,7,0.0,13.71),
    ("sprinkler systems installation eagle idaho",0,7,0.0,16.43),
    ("winterize sprinkler caldwell",0,7,0.0,20.57),
    ("lawn irrigation repair nampa",0,5,0.0,6.2),
    ("sprinkler repair kuna",0,5,0.0,5.0),
    ("sprinklers repair near me",0,5,0.0,6.4),
    ("sprinkler adjustment near me",0,5,0.0,6.8),
    ("winterize sprinkler nampa",0,5,0.0,9.4),
    ("sprinkler spring startup near me",0,5,0.0,11.4),
    ("sprinklers boise",0,5,0.0,15.2),
    ("irrigation repair boise",0,5,0.0,20.8),
    ("sprinkler blowout boise idaho",0,5,0.0,23.2),
    ("sprinkler system installation near me",0,5,0.0,28.6),
    ("water sprinkler system meridian id",0,5,0.0,33.0),
    ("irrigation installation boise",0,6,0.0,38.33),
    ("lawn sprinkler",0,4,0.0,2.75),
    ("sprinkler repair meridian id",0,4,0.0,3.75),
    ("yard sprinkler repair near me",0,4,0.0,5.75),
    ("sprinkler pipe repair near me",0,4,0.0,6.5),
    ("sprinkler pump repair near me",0,4,0.0,7.5),
    ("irrigation service near me",0,4,0.0,8.25),
    ("24 hour sprinkler repair near me",0,4,0.0,9.0),
    ("star irrigation",0,4,0.0,9.5),
    ("sprinkler repair kuna idaho",0,4,0.0,10.0),
    ("irrigation service",0,4,0.0,10.75),
    ("irrigation management services nampa",0,4,0.0,11.0),
    ("boise sprinkler service",0,4,0.0,11.75),
    ("meridian idaho sprinkler repair",0,4,0.0,12.0),
    ("boise sprinkler turn on",0,4,0.0,14.0),
    ("meridian sprinkler system repair",0,4,0.0,17.5),
    ("idaho sprinkler",0,4,0.0,18.25),
    ("sprinkler blow out boise idaho",0,4,0.0,22.75),
    ("sprinkler blowouts meridian idaho",0,4,0.0,35.5),
    ("sprinkler installation",0,3,0.0,1.0),
    ("sprinkler valve repair",0,3,0.0,2.0),
    ("fix sprinkler head",0,3,0.0,3.0),
    ("irrigation system",0,3,0.0,3.0),
    ("sprinkler system boise",0,3,0.0,5.67),
    ("sprinkler turn on service",0,3,0.0,5.67),
    ("irrigation sprinkler system repair",0,3,0.0,6.67),
    ("sprinkler company boise",0,3,0.0,6.67),
    ("sprinkler maintenance",0,3,0.0,6.67),
    ("sprinkler repairs near me",0,3,0.0,6.67),
    ("irrigation system installation nampa",0,3,0.0,7.0),
    ("drip irrigation",0,3,0.0,8.67),
    ("lawn sprinkler companies near me",0,3,0.0,9.33),
    ("sprinkler turn on boise",0,3,0.0,10.33),
    ("lawn sprinkler service",0,3,0.0,10.67),
    ("sprinkler valve",0,3,0.0,10.67),
    ("irrigation system design nampa",0,3,0.0,11.0),
    ("sprinkler boise",0,3,0.0,18.0),
    ("sprinkler installation boise id",0,3,0.0,19.0),
    ("sprinkler system installation boise",0,3,0.0,20.0),
    ("meridian irrigation winterization",0,3,0.0,20.67),
    ("boise idaho sprinkler blowout",0,3,0.0,21.33),
    ("sprinkler blowouts boise",0,3,0.0,36.0),
    ("eagle sprinkler",0,3,0.0,40.0),
    ("eagle sprinklers",0,3,0.0,45.67),
    ("water line replacement caldwell id",0,3,0.0,53.33),
    ("boise sprinkler guy",0,3,0.0,42.67),
    ("drip irrigation installation meridian",0,2,0.0,1.0),
    ("fix sprinkler system",0,2,0.0,1.0),
    ("irrigation contractors near me",0,2,0.0,1.0),
    ("lawn irrigation repair near me",0,2,0.0,1.0),
    ("sprinkler blowout companies near me",0,2,0.0,1.0),
    ("lawn sprinkler repair service",0,2,0.0,1.5),
    ("new sprinkler system",0,2,0.0,1.5),
    ("sprinkler technician near me",0,2,0.0,2.0),
    ("sprinkler repair companies near me",0,2,0.0,4.0),
    ("boise sprinkler companies",0,2,0.0,4.5),
    ("underground sprinkler repair near me",0,2,0.0,4.5),
    ("best sprinkler repair near me",0,2,0.0,5.5),
    ("irrigation pump repair near me",0,2,0.0,5.5),
    ("same day sprinkler repair",0,2,0.0,5.5),
    ("nampa sprinkler blowouts",0,2,0.0,6.5),
    ("irrigation maintenance near me",0,2,0.0,7.0),
    ("sprinkler system repairs",0,2,0.0,7.0),
    ("irrigation turn on near me",0,2,0.0,7.5),
    ("sprinkler valve rebuild",0,2,0.0,7.5),
    ("underground sprinkler head replacement",0,2,0.0,7.5),
    ("fixing sprinkler heads",0,2,0.0,8.5),
    ("rainbird repair near me",0,2,0.0,10.0),
    ("lawn irrigation system repair near me",0,2,0.0,11.0),
    ("sprinkler contractor",0,2,0.0,11.5),
    ("meridian winterize sprinkler system",0,2,0.0,14.0),
    ("sprinkler box full of water",0,2,0.0,18.5),
    ("sprinkler blowout kuna",0,2,0.0,19.0),
    ("sprinkler and irrigation installation eagle",0,2,0.0,21.0),
    ("meridian idaho sprinkler blowout",0,2,0.0,25.5),
    ("irrigation installation boise idaho",0,2,0.0,26.5),
    ("irrigation valve box full of water",0,2,0.0,27.0),
    ("boise idaho sprinkler repair",0,2,0.0,36.5),
    ("water line repair meridian id",0,2,0.0,48.5),
    ("commercial sprinkler services",0,2,0.0,59.0),
    ("best sprinkler installation near me",0,1,0.0,1.0),
    ("best sprinkler service near me",0,1,0.0,1.0),
    ("broken sprinkler head repair",0,1,0.0,1.0),
    ("commercial irrigation contractors near me",0,1,0.0,1.0),
    ("drip irrigation installation nampa",0,1,0.0,1.0),
    ("emergency sprinkler repair near me",0,1,0.0,1.0),
    ("home sprinkler repair",0,1,0.0,1.0),
    ("irrigation system maintenance",0,1,0.0,1.0),
    ("irrigation system maintenance near me",0,1,0.0,1.0),
    ("residential sprinkler repair",0,1,0.0,1.0),
    ("sprinkler repair services near me",0,1,0.0,1.0),
    ("sprinkler system installation nampa",0,1,0.0,1.0),
    ("irrigation line repair",0,1,0.0,2.0),
    ("residential sprinkler service near me",0,1,0.0,2.0),
    ("sprinkler head repair",0,1,0.0,2.0),
    ("eagle irrigation",0,1,0.0,11.0),
    ("irrigation company meridian",0,1,0.0,12.0),
    ("sprinkler blowout caldwell idaho",0,1,0.0,15.0),
    ("valve box full of water",0,1,0.0,23.0),
    ("sprinkler valve repair near me",0,1,0.0,24.0),
    ("sprinkler blowout service near me",0,1,0.0,23.0),
    ("treasure valley irrigation systems",0,1,0.0,35.0),
    ("sprinkler troubleshooting",0,1,0.0,41.0),
    ("water line repair kuna id",0,1,0.0,42.0),
    ("irrigation system design caldwell",0,1,0.0,43.0),
    ("garden city sprinkler repair",0,1,0.0,1.0), # Garden City = Boise area
    ("in ground sprinkler system",0,1,0.0,2.0),
    ("in ground sprinklers",0,2,0.0,5.5),
    ("same day sprinkler repair near me",0,1,0.0,5.0),
    ("repair sprinkler head",0,2,0.0,3.0),
    ("sprinkler controller",0,2,0.0,3.0),
    ("irrigation installation near me",0,2,0.0,3.5),
    ("top rated sprinkler companies near me",0,2,0.0,1.0),
    ("lawn sprinkler system contractor",0,2,0.0,4.5),
    ("sprinkler blow out",0,2,0.0,5.0),
    ("sprinkler guards",0,2,0.0,6.0),
    ("sprinkler replacement heads",0,2,0.0,6.0),
    ("sprinkler system repair nearby",0,2,0.0,6.0),
    ("sprinkler services near me",0,2,0.0,8.0),
    ("replacement sprinkler valve",0,2,0.0,9.0),
    ("sprinkler zone low pressure",0,2,0.0,48.5),
    ("low pressure in sprinkler system",0,2,0.0,65.0),
    ("sprinkler repair eagle",0,12,0.0,16.33),
    ("star irrigation",0,4,0.0,9.5),
    ("water line repair near me",0,7,0.0,68.57),
    ("sprinkler head replacement",0,18,0.0,6.22),
    ("dead spots",0,3,0.0,53.67),
    ("sprinkler system low pressure",0,1,0.0,66.0),
    ("low pressure sprinkler zone",0,1,0.0,38.0),
    ("water in sprinkler valve box",0,1,0.0,39.0),
    ("why is there water in my sprinkler valve box",0,1,0.0,33.0),
    ("sprinkler system valve box full of water",0,1,0.0,25.0),
    ("how to keep water out of irrigation valve box",0,1,0.0,3.0),
    ("sprinkler head shooting water straight up",0,1,0.0,47.0),
    ("lawn sprinkler not working",0,1,0.0,61.0),
    ("how to fix wet spot in yard",0,1,0.0,52.0),
    ("large dead spot in lawn",0,1,0.0,68.0),
]

# Remove duplicates by keeping first occurrence per query
seen = set()
data = []
for row in raw:
    if row[0] not in seen:
        seen.add(row[0])
        data.append(row)

# Sort by impressions desc, then clicks desc
data.sort(key=lambda x: (-x[2], -x[1]))

# --- Build optimization list ---
optimize = [
    # (query, impressions, position, priority, page_to_target, action)
    ("sprinkler repair nampa", 305, 3.98, "🔥 Top Priority", "nampa-sprinkler-repair.html", "Already ranking #4 — push to #1-2 with more backlinks + reviews mentioning Nampa"),
    ("sprinkler repair near me", 283, 8.12, "🔥 Top Priority", "index.html / all city pages", "Position 8 with 283 impressions — improve homepage title tag, add more 'near me' language in H1/meta"),
    ("sprinkler repair boise", 157, 7.23, "🔥 Top Priority", "boise-sprinkler-repair.html", "157 impressions at pos 7 — needs more content, internal links, and local backlinks"),
    ("sprinkler repair", 131, 8.27, "🔥 Top Priority", "index.html", "Broad head term — homepage needs to rank higher here"),
    ("sprinkler system repair", 91, 7.26, "🔥 Top Priority", "sprinkler-repair.html", "91 impressions at pos 7 — solid service page opportunity"),
    ("sprinkler blowout nampa", 89, 9.37, "🔥 Top Priority", "winterization.html + nampa page", "89 impressions pos 9 — blowout season coming, add Nampa-specific blowout content"),
    ("sprinkler repair meridian", 103, 8.93, "🔥 Top Priority", "meridian-sprinkler-repair.html", "Ranking #9 with 103 impressions and 7 clicks — improve title/H1 with exact phrase"),
    ("irrigation repair near me", 65, 9.18, "🔥 Top Priority", "index.html / sprinkler-repair.html", "65 impressions pos 9 — add 'irrigation repair' language to homepage"),
    ("sprinkler blowout near me", 39, 9.51, "High Value", "winterization.html", "39 impressions pos 9.5 — winterization page needs more 'blowout near me' optimization"),
    ("sprinkler systems installation nampa", 31, 3.03, "High Value", "nampa-sprinkler-repair.html", "Position 3 with 31 impressions but 0 clicks — fix title/meta to get the click"),
    ("sprinkler blowout meridian", 48, 28.12, "High Value", "meridian-sprinkler-repair.html + winterization.html", "48 impressions but pos 28 — add blowout section to Meridian city page"),
    ("irrigation system repair meridian", 52, 27.83, "High Value", "meridian-sprinkler-repair.html", "52 impressions pos 28 — add more irrigation repair content to Meridian page"),
    ("sprinkler repair caldwell", 68, 4.44, "High Value", "caldwell-sprinkler-repair.html", "68 impressions at pos 4.4 — very close to top 3, needs a push"),
    ("sprinkler installation near me", 36, 5.56, "High Value", "sprinkler-installation.html", "Already in top 6 — installation page needs more 'near me' optimization"),
    ("sprinkler repair eagle idaho", 24, 16.04, "High Value", "eagle-sprinkler-repair.html", "Pos 16 — Eagle page needs more content and internal links from homepage"),
    ("nampa sprinkler blowout", 26, 15.92, "High Value", "nampa-sprinkler-repair.html + winterization.html", "26 impressions pos 16 — add blowout section to Nampa page"),
    ("sprinkler head replacement", 18, 6.22, "High Value", "sprinkler-head-replacement-treasure-valley.html", "Pos 6 with 18 impressions — head replacement page needs stronger title tag"),
    ("irrigation repair",50,10.3,"High Value","sprinkler-repair.html / index.html","50 impressions pos 10 — use 'irrigation repair' more in service page copy"),
    ("sprinkler repair meridian idaho",47,9.64,"High Value","meridian-sprinkler-repair.html","47 impressions pos 9.6 — very close to page 1 top, push Meridian page harder"),
    ("sprinkler repair eagle",12,16.33,"Grow","eagle-sprinkler-repair.html","12 impressions pos 16 — Eagle page needs internal link boost"),
    ("sprinkler repair kuna",5,5.0,"Grow","kuna-sprinkler-repair.html","Pos 5 — Kuna page is close, needs more reviews and links"),
    ("sprinkler repair kuna idaho",4,10.0,"Grow","kuna-sprinkler-repair.html","Pos 10 — optimize Kuna page title/meta with exact match"),
    ("sprinkler winterization near me",12,20.83,"Grow","winterization.html","12 impressions pos 21 — winterization page needs 'near me' language"),
    ("emergency sprinkler repair",12,10.5,"Grow","emergency.html","12 impressions pos 10 — good page to have, needs optimization"),
    ("sprinkler blowout caldwell",13,15.38,"Grow","caldwell-sprinkler-repair.html","Add blowout content to Caldwell city page"),
    ("sprinkler systems installation star idaho",28,13.96,"Grow","star-sprinkler-repair.html","28 impressions pos 14 — Star page needs installation content"),
    ("sprinkler systems installation caldwell",25,13.36,"Grow","caldwell-sprinkler-repair.html","25 impressions pos 13 — add installation section to Caldwell page"),
    ("irrigation systems nampa",27,1.59,"Grow","nampa-sprinkler-repair.html","Pos 1.6 — showing up near top but 0 clicks, fix meta description"),
    ("sprinkler blowout boise",26,40.5,"Long Term","boise-sprinkler-repair.html + winterization.html","Pos 40 — add blowout content to Boise city page"),
    ("backflow testing nampa",0,0,"New Page","backflow.html","Not showing yet — add Nampa-specific backflow content to backflow page"),
    ("sprinkler valve repair nampa",0,0,"New Page","valve-repair-treasure-valley.html","Not showing yet — needs Nampa-specific valve content"),
    ("sprinkler controller replacement boise",0,0,"New Page","controller-replacement.html","Not showing yet — add more city-specific controller content"),
]

wb = openpyxl.Workbook()

# ---- COLORS ----
GREEN_DARK = "1a5c1a"
GREEN_MED = "2d7a2d"
GREEN_LIGHT = "e8f5e8"
WHITE = "FFFFFF"
GRAY_HEADER = "f0f0f0"
YELLOW = "FFF9C4"
RED_LIGHT = "FFEBEE"
ORANGE_LIGHT = "FFF3E0"

def thin_border():
    thin = Side(style='thin', color='CCCCCC')
    return Border(left=thin, right=thin, top=thin, bottom=thin)

# ================== SHEET 1: Cleaned Queries ==================
ws1 = wb.active
ws1.title = "Cleaned Queries"

headers = ["Query", "Clicks", "Impressions", "CTR %", "Avg Position"]
col_widths = [55, 10, 14, 10, 14]

# Header row
for col, (h, w) in enumerate(zip(headers, col_widths), 1):
    cell = ws1.cell(row=1, column=col, value=h)
    cell.font = Font(bold=True, color=WHITE, name="Arial", size=10)
    cell.fill = PatternFill("solid", fgColor=GREEN_DARK)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = thin_border()
    ws1.column_dimensions[get_column_letter(col)].width = w

ws1.row_dimensions[1].height = 22

for row_idx, (query, clicks, impressions, ctr, pos) in enumerate(data, 2):
    fill_color = WHITE if row_idx % 2 == 0 else GREEN_LIGHT
    vals = [query, clicks, impressions, round(ctr, 2), round(pos, 2)]
    for col, val in enumerate(vals, 1):
        cell = ws1.cell(row=row_idx, column=col, value=val)
        cell.font = Font(name="Arial", size=9)
        cell.fill = PatternFill("solid", fgColor=fill_color)
        cell.border = thin_border()
        if col == 1:
            cell.alignment = Alignment(horizontal="left", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="center", vertical="center")
    # Color code by clicks
    if clicks >= 5:
        ws1.cell(row=row_idx, column=2).fill = PatternFill("solid", fgColor="C8E6C9")
    elif clicks == 0 and impressions >= 30:
        ws1.cell(row=row_idx, column=3).fill = PatternFill("solid", fgColor="FFE0B2")

# Freeze header
ws1.freeze_panes = "A2"

# ================== SHEET 2: Optimize For ==================
ws2 = wb.create_sheet("Optimize For")

opt_headers = ["Query", "Impressions", "Avg Position", "Priority", "Target Page", "Action / Notes"]
opt_widths = [42, 13, 14, 16, 45, 70]

for col, (h, w) in enumerate(zip(opt_headers, opt_widths), 1):
    cell = ws2.cell(row=1, column=col, value=h)
    cell.font = Font(bold=True, color=WHITE, name="Arial", size=10)
    cell.fill = PatternFill("solid", fgColor=GREEN_DARK)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border()
    ws2.column_dimensions[get_column_letter(col)].width = w

ws2.row_dimensions[1].height = 22

priority_colors = {
    "🔥 Top Priority": "FFCDD2",
    "High Value": "FFE0B2",
    "Grow": "FFF9C4",
    "Long Term": "E8F5E9",
    "New Page": "E3F2FD",
}

for row_idx, (query, impressions, position, priority, page, action) in enumerate(optimize, 2):
    vals = [query, impressions, position, priority, page, action]
    bg = priority_colors.get(priority, WHITE)
    for col, val in enumerate(vals, 1):
        cell = ws2.cell(row=row_idx, column=col, value=val)
        cell.font = Font(name="Arial", size=9)
        cell.fill = PatternFill("solid", fgColor=bg)
        cell.border = thin_border()
        if col in [1, 5, 6]:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[row_idx].height = 30

ws2.freeze_panes = "A2"

# Legend
legend_row = len(optimize) + 3
ws2.cell(row=legend_row, column=1, value="Priority Legend").font = Font(bold=True, name="Arial", size=9)
legend_items = [
    ("🔥 Top Priority", "FFCDD2", "High impressions, ranking 5-10 — small push gets top 3"),
    ("High Value", "FFE0B2", "Good impressions, ranking 10-20 — solid content improvements needed"),
    ("Grow", "FFF9C4", "Lower impressions or ranking 15-25 — build these up over time"),
    ("Long Term", "E8F5E9", "Ranking 30+ — needs significant work but worth targeting"),
    ("New Page", "E3F2FD", "Not showing up yet — create or improve dedicated page"),
]
for i, (label, color, note) in enumerate(legend_items):
    r = legend_row + 1 + i
    c1 = ws2.cell(row=r, column=1, value=label)
    c1.fill = PatternFill("solid", fgColor=color)
    c1.font = Font(name="Arial", size=9, bold=True)
    c1.border = thin_border()
    c2 = ws2.cell(row=r, column=2, value=note)
    c2.font = Font(name="Arial", size=9)
    ws2.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    c2.alignment = Alignment(horizontal="left")

output = "/sessions/charming-confident-dirac/mnt/Building Beeline Website/Beeline_GSC_Queries_Cleaned.xlsx"
wb.save(output)
print("Saved:", output)
