import json
def template(d):
    return f"""
    <div class="film" style="display: block">
        <div class="pres">
            <div class="poster">
                <img src="{d['image']}" alt="photo">
            </div>
            <div class="desc">
                <h3 style="text-align: center"><a href="{d['imdb']}">{d['director']}</a></h3>
                <hr>
                <div class="dirfilm">
                    <a href="{d['l1']}" title="{d['f1']}"><img src="{d['i1']}" alt="{d['f1']}"></a>
                    <a href="{d['l2']}" title="{d['f2']}"><img src="{d['i2']}" alt="{d['f2']}"></a>
                    <a href="{d['l3']}" title="{d['f3']}"><img src="{d['i3']}" alt="{d['f3']}"></a>
                    <a href="{d['l4']}" title="{d['f4']}"><img src="{d['i4']}" alt="{d['f4']}"></a>
                </div>
            </div>
        </div>
    </div>
    """

with open('directors.json', 'r', encoding="utf8") as file:
    data = file.read()

output=""
for director in json.loads(data):
    output+=template(director)

with open('out.txt', 'w+', encoding="utf8") as out:
    out.write(output)
