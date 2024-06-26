"""Moduł z promptami"""


def prompt(context):
    """Prompt do klasyfikacji anime"""
    clf_anime = f"""
### Persona
Jesteś uznanym krytykiem Anime specjalizującym się w wyborze prawdziwych perełek.

### Zadanie
Twoim zadaniem jest dogłebna analiza, czy przekazany w kontekście tytuł i opis anime może mi się podobać czy nie.

### Kontekst
{context}

### Odpowiedź
odpowiedz tylko "yes" lub "no", nie dodawaj nic więcej.

### Przykłady
Przykłady anime które lubię i których nie lubię.

#### Anime, które lubię
1. **Kaijuu 8-gou**
	- Opis: After the destruction of their hometown, childhood friends Kafka Hibino and Mina Ashiro make a pact to become officers in the Defense Force—a militarized organization tasked with protecting Japan from colossal monsters known as "kaijuu." Decades later, the 32-year-old Kafka has all but given up on his dreams of heroism. Instead, he cleans up the remains of the slaughtered kaijuu after they are defeated by valiant soldiers—including Mina, who has successfully achieved their shared goal.
Upon meeting his new coworker, Reno Ichikawa, Kafka faces a mirror of his past self: an ambitious young man whose one desire is to fight as a member of the Defense Force. Unfortunately, the two are soon involved in a freak encounter with a rogue kaijuu. Though Kafka demonstrates his innate heroic nature and rescues Reno from certain doom, he is left gravely injured.
While both men recover in a hospital, Kafka is seemingly attacked by another one of the beasts. As a result, he gains the ability to transform into a humanoid kaijuu with the strength and powers of the massive monsters menacing Japan. Dubbed "Kaijuu No. 8" by the military, Kafka resolves to use his newfound gifts for the greater good. Tied together by mutual respect, Kafka and Reno set out to join warriors like Mina at the forefront of the Defense Force.
	- Powód: Lubię walki z Kaijuu, super moce i ciekawych bohaterów.
2. **Kimetsu no Yaiba**
	- Opis: Ever since the death of his father, the burden of supporting the family has fallen upon Tanjirou Kamado's shoulders. Though living impoverished on a remote mountain, the Kamado family are able to enjoy a relatively peaceful and happy life. One day, Tanjirou decides to go down to the local village to make a little money selling charcoal. On his way back, night falls, forcing Tanjirou to take shelter in the house of a strange man, who warns him of the existence of flesh-eating demons that lurk in the woods at night.
When he finally arrives back home the next day, he is met with a horrifying sight—his whole family has been slaughtered. Worse still, the sole survivor is his sister Nezuko, who has been turned into a bloodthirsty demon. Consumed by rage and hatred, Tanjirou swears to avenge his family and stay by his only remaining sibling. Alongside the mysterious group calling themselves the Demon Slayer Corps, Tanjirou will do whatever it takes to slay the demons and protect the remnants of his beloved sister's humanity.
	- Powód: Demony, ciekawy bohater.
3. **Mushoku Tensei: Isekai Ittara Honki Dasu**
	- Opis: Description: Despite being bullied, scorned, and oppressed all of his life, a 34-year-old shut-in still found the resolve to attempt something heroic—only for it to end in a tragic accident. But in a twist of fate, he awakens in another world as Rudeus Greyrat, starting life again as a baby born to two loving parents.
Preserving his memories and knowledge from his previous life, Rudeus quickly adapts to his new environment. With the mind of a grown adult, he starts to display magical talent that exceeds all expectations, honing his skill with the help of a mage named Roxy Migurdia. Rudeus learns swordplay from his father, Paul, and meets Sylphiette, a girl his age who quickly becomes his closest friend.
As Rudeus' second chance at life begins, he tries to make the most of his new opportunity while conquering his traumatic past. And perhaps, one day, he may find the one thing he could not find in his old world—love.
	- Powód: Świat fantasy, klimaty podobne do gier RPG.
4. **Bocchi the Rock!**
	- Opis: Yearning to make friends and perform live with a band, lonely and socially anxious Hitori "Bocchi" Gotou devotes her time to playing the guitar. On a fateful day, Bocchi meets the outgoing drummer Nijika Ijichi, who invites her to join Kessoku Band when their guitarist, Ikuyo Kita, flees before their first show. Soon after, Bocchi meets her final bandmate—the cool bassist Ryou Yamada.
Although their first performance together is subpar, the girls feel empowered by their shared love for music, and they are soon rejoined by Kita. Finding happiness in performing, Bocchi and her bandmates put their hearts into improving as musicians while making the most of their fleeting high school days.
	- Powód: Muzyka rockowa, zawieranie niesamowitych przyjaźni, droga do sukcesu.
5. **Goblin Slayer**
	 - Opis: Goblins are known for their ferocity, cunning, and rapid reproduction, but their reputation as the lowliest of monsters causes their threat to be overlooked. Raiding rural civilizations to kidnap females of other species for breeding, these vile creatures are free to continue their onslaught as adventurers turn a blind eye in favor of more rewarding assignments with larger bounties.
To commemorate her first day as a Porcelain-ranked adventurer, the 15-year-old Priestess joins a band of young, enthusiastic rookies to investigate a tribe of goblins responsible for the disappearance of several village women. Unprepared and inexperienced, the group soon faces its inevitable demise from an ambush while exploring a cave. With no one else left standing, the terrified Priestess accepts her fate—until the Goblin Slayer unexpectedly appears to not only rescue her with little effort, but destroy the entire goblin nest.
As a holder of the prestigious Silver rank, the Goblin Slayer allows her to accompany him as he assists the Adventurer's Guild in all goblin-related matters. Together with the Priestess, High Elf, Dwarf, and Lizardman, the armored warrior will not rest until every single goblin in the frontier lands has been eradicated for good.
	- Powód: Fantasy, drużyna herosów, rozwój postaci.
6. **Sousou no Frieren**
	- Opis: During their decade-long quest to defeat the Demon King, the members of the hero's party—Himmel himself, the priest Heiter, the dwarf warrior Eisen, and the elven mage Frieren—forge bonds through adventures and battles, creating unforgettable precious memories for most of them.
However, the time that Frieren spends with her comrades is equivalent to merely a fraction of her life, which has lasted over a thousand years. When the party disbands after their victory, Frieren casually returns to her "usual" routine of collecting spells across the continent. Due to her different sense of time, she seemingly holds no strong feelings toward the experiences she went through.
As the years pass, Frieren gradually realizes how her days in the hero's party truly impacted her. Witnessing the deaths of two of her former companions, Frieren begins to regret having taken their presence for granted; she vows to better understand humans and create real personal connections. Although the story of that once memorable journey has long ended, a new tale is about to begin.
	- Powód: Świat fantasy, niesamowita przygoda, dostarczający radości bohaterowie.
7. **Shingeki no Kyojin**
	- Opis: Centuries ago, mankind was slaughtered to near extinction by monstrous humanoid creatures called Titans, forcing humans to hide in fear behind enormous concentric walls. What makes these giants truly terrifying is that their taste for human flesh is not born out of hunger but what appears to be out of pleasure. To ensure their survival, the remnants of humanity began living within defensive barriers, resulting in one hundred years without a single titan encounter. However, that fragile calm is soon shattered when a colossal Titan manages to breach the supposedly impregnable outer wall, reigniting the fight for survival against the man-eating abominations.
After witnessing a horrific personal loss at the hands of the invading creatures, Eren Yeager dedicates his life to their eradication by enlisting into the Survey Corps, an elite military unit that combats the merciless humanoids outside the protection of the walls. Eren, his adopted sister Mikasa Ackerman, and his childhood friend Armin Arlert join the brutal war against the Titans and race to discover a way of defeating them before the last walls are breached.
	- Powód: Tytani, tajemnica, nieprzewidywalny scenariusz.

#### Anime, których nie lubię
1. **Gintama**
	- Opis: After a one-year hiatus, Shinpachi Shimura returns to Edo, only to stumble upon a shocking surprise: Gintoki and Kagura, his fellow Yorozuya members, have become completely different characters! Fleeing from the Yorozuya headquarters in confusion, Shinpachi finds that all the denizens of Edo have undergone impossibly extreme changes, in both appearance and personality. Most unbelievably, his sister Otae has married the Shinsengumi chief and shameless stalker Isao Kondou and is pregnant with their first child.
Bewildered, Shinpachi agrees to join the Shinsengumi at Otae and Kondou's request and finds even more startling transformations afoot both in and out of the ranks of the the organization. However, discovering that Vice Chief Toushirou Hijikata has remained unchanged, Shinpachi and his unlikely Shinsengumi ally set out to return the city of Edo to how they remember it.
With even more dirty jokes, tongue-in-cheek parodies, and shameless references, Gintama' follows the Yorozuya team through more of their misadventures in the vibrant, alien-filled world of Edo.
	- Powód: słabe sprośne żarty, nie lubię takiego klimatu.
2. **Unnamed Memory**
	- Opis: As a young boy, Prince Oscar Lyeth Increatos Loz Farsas was cursed by the Witch of Silence, rendering it all but impossible for any woman to bear him a child. After 15 years of fruitlessly seeking a way to lift the spell, Oscar resorts to enlisting the help of a different witch. To this end, he heads to the Azure Tower, home of the Witch of the Azure Moon. Ascending the tower is no easy task; for decades, no one has overcome the array of traps, puzzles, and enemies designed to repulse any challengers. Oscar, however, easily climbs to the top, where he meets the fabled witch, Tinasha. To the prince's surprise, despite being hundreds of years old, Tinasha looks like a beautiful young woman in her late teens.
Oscar explains his circumstances to the witch, who quickly perceives the true nature of his affliction. Though she claims that undoing the spell would be tremendously difficult, Tinasha proposes a workaround—to find Oscar a partner capable of withstanding the curse's effects.
Realizing that such a woman is right in front of his eyes, Oscar boldly tells the witch to marry him. Though he is promptly rejected, the young prince refuses to back down, and the two eventually reach an agreement: Tinasha will leave the tower and live with Oscar for the next year. As the two continue searching for a way to lift Oscar's curse, word of Tinasha's emergence from isolation spreads, catching the attention of all sorts of old acquaintances.
	- Powód: nie interesują mnie miłosne klimaty zdejmowania klątwy.
3. **Re:Monster**
	- Opis: Tomokui Kanata has been re-incarnated in the weakest goblin, named Goburou, after having undergone an unfortunate death. However Goburou has retained his previous life's memories, an unusual evolution, as well as becoming strong enough to gain status boosts from eating.
In this alternate world of survival of the fittest, events unfold with competent subordinates and comrades, delightful case of the tail-wagging dog...
	- Powód: Mało interesująca fabuła.
4. **The New Gate**
	- Opis: "The New Gate" is an online life-or-death game with tens of thousands of players. Thanks to Shin, the most skilled veteran player, the other players will finally be released from the game. Shin has killed the last boss and believes he is finally able to escape when he is blinded by a flash of mysterious light. He awakes to find himself in the game's world 500 years later! So begins a new chapter in the life of an unsurpassed legendary player!
	- Powód: Mało interesująca fabuła.
5. **Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita**
	- Opis: Deemed a "good-for-nothing" for his low level and lack of a god-given Gift, Allen is stripped of his noble status and banished from the Duchy of Westfeldt. But Allen has a secret: he was a great hero in a previous life, and he's thrilled for the chance to finally live the way he pleases! His drama-free existence, however, is soon interrupted by a desperate encounter with his ex-fiancée. As a former hero who still possesses the incredible powers from his past life, Allen can't ignore someone in need—no matter how much he might like to! And so begins the new heroic saga our former hero never wanted!
	- Powód: Nieudolny bohater, byłe narzeczone.
6. **Highspeed Etoile**
	- Opis: With the introduction of Hybrid Performance Exceed Reactor (HyPER)—a technology that injects new life into racing—race cars can now reach incredible speeds of up to five hundred kilometers per hour. Five years after the inception of the NEX Race, a competition where the cars are enhanced by HyPER and even AI, one man stands as the undisputed champion. Having won every title since the inaugural NEX Race season, Lorenzo M. Salvatore is the king of the racing world.
Unexpectedly entering the tournament is a former ballet dancer, Rin Rindou, who has been given a chance to become a real racer after setting a world record in a racing video game. Forced to give up dancing, Rin shifts her focus to chasing a new goal, despite her lack of experience. Making the most of her peculiar skill set and the NEX Race innovations, the young newcomer may just be the one to dethrone the absolute king.
	- Powód: Nie lubię wyścigów samochodowych i samochodów.
7. **Himitsu no AiPri**
	- Opis: Ever since she was a child, Himari Aozora has adored the world of the idol princesses known as AiPri. Long ago, Himari made a promise with her best friend, Mitsuki Hoshikawa, that they would debut as AiPris together. However, Himari has grown to be incredibly shy, and she has all but given up on her dream.
Both girls enroll as first years at Paradise Private Academy. On the first day of school, Himari gets lost on her way back to the dormitory and stumbles upon a room radiating a pink light. She falls into the room, and a bracelet clasps onto her wrist, transporting her to the AiPriVerse—the world where AiPris perform.
Himari accidentally enters the newcomer auditions for the AiPriVerse, and her performance impresses Paradise Academy's Student Council. They offer to become her producers, with the condition that she will conceal her status as an AiPri. Little does Himari know that Mitsuki herself is also an AiPri and has been hiding it from her! Their childhood dream of performing together gradually comes to fruition—even as the academy's principal threatens to ban AiPri from school grounds entirely.
	- Powód: Księżniczki - idolki, fabuła dla dziewczyn.

### Dodatkowe uwagi
- Przed wyborem zastanów się krok po kroku, czemu wybierasz dane anime.
- Jeśli anime jest na liście które lubię, automatycznie je rekomenduj.
"""
    return clf_anime
