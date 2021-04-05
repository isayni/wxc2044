import json
def template(f):
    return f"""
    <div class="film">
        <div class="pres">
            <div class="poster">
                <img src="{f['poster']}" alt="poster">
            </div>
            <div class="desc">
                    <h3><a href="{f['web']}">{f['title']}</a> ({f['year']})</h3>
                <hr align="left">
                <div class="ratings">
                    <div class="rating">
                        <img src="img/imdb.png">
                        <p>{f['i']}</p>
                    </div>
                    <div class="rating">
                        <img src="img/filmweb.png">
                        <p>{f['f']}</p>
                    </div>
                    <div class="rating">
                        <img src="img/rotten.png">
                        <p>{f['r']}%</p>
                    </div>
                    <div class="rating">
                        <img src="img/meta.png">
                        <p class="metar">{f['m']}</p>
                    </div>
                </div>
                <div class="cred">
                    <p>Reżyseria: {f['dir']}</p>
                    <p>Obsada: {f['cast']}</p>
                </div>
            </div>
        </div>
        <div class="image">
            <img src="{f['pic']}" alt="picture">
        </div>
    </div>
    """

with open('data.json', 'r', encoding="utf8") as file:
    data = file.read()
    
output=""
for film in json.loads(data):
    output+=template(film)
    
with open('out.txt', 'w+', encoding="utf8") as out:
    out.write(output)