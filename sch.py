import json
def template(title, year, poster, web, i, f, r, m, dir, cast, pic):
    return f"""
    <div class="film">
        <div class="pres">
            <div class="poster">
                <img src="{poster}" alt="poster">
            </div>
            <div class="desc">
                    <h3><a href="{web}">{title}</a> ({year})</h3>
                <hr align="left">
                <div class="ratings">
                    <div class="rating">
                        <img src="img/imdb.png">
                        <p>{i}</p>
                    </div>
                    <div class="rating">
                        <img src="img/filmweb.png">
                        <p>{f}</p>
                    </div>
                    <div class="rating">
                        <img src="img/rotten.png">
                        <p>{r}%</p>
                    </div>
                    <div class="rating">
                        <img src="img/meta.png">
                        <p class="metar">{m}</p>
                    </div>
                </div>
                <div class="cred">
                    <p>Reżyseria: {dir}</p>
                    <p>Obsada: {cast}</p>
                </div>
            </div>
        </div>
        <div class="image">
            <img src="{pic}" alt="picture">
        </div>
    </div>
    """

with open('data.json', 'r', encoding="utf8") as file:
    data = file.read()
    
output=""
for film in json.loads(data):
    output+=template(film['title'], film['year'], film['poster'], film['web'], film['i'], film['f'], film['r'], film['m'], film['dir'], film['cast'], film['pic'])
    
with open('out.txt', 'w+', encoding="utf8") as out:
    out.write(output)