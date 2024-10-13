--
-- PostgreSQL database dump
--

-- Dumped from database version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: characters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters (
    id integer NOT NULL,
    birth_year character varying,
    eye_color character varying,
    films text,
    gender character varying,
    hair_color character varying,
    height character varying,
    homeworld character varying,
    mass character varying,
    name character varying,
    skin_color character varying,
    species text,
    starships text,
    vehicles text
);


ALTER TABLE public.characters OWNER TO postgres;

--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.characters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.characters_id_seq OWNER TO postgres;

--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.characters_id_seq OWNED BY public.characters.id;


--
-- Name: characters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters ALTER COLUMN id SET DEFAULT nextval('public.characters_id_seq'::regclass);


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.characters (id, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles) FROM stdin;
9	24BBY	brown	A New Hope	male	black	183	Tatooine	84	Biggs Darklighter	light			
30	8BBY	brown	Return of the Jedi	male	brown	88	Endor	20	Wicket Systri Warrick	brown	Ewok		
5	19BBY	brown	A New Hope, The Empire Strikes Back, Return of the Jedi	female	brown	150	Alderaan	49	Leia Organa	light			Imperial Speeder Bike
19	unknown	blue	A New Hope	male	brown	180	Bestine IV	110	Jek Tono Porkins	fair		X-wing	
20	896BBY	brown	The Empire Strikes Back, Return of the Jedi, The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	white	66	unknown	17	Yoda	green	Yoda's species		
1	19BBY	blue	The Empire Strikes Back, Return of the Jedi	male	blond	172	Tatooine	77	Luke Skywalker	fair		X-wing, Imperial shuttle	Snowspeeder, Imperial Speeder Bike
7	47BBY	blue	Revenge of the Sith	female	brown	165	Tatooine	75	Beru Whitesun lars	light			
14	29BBY	brown	A New Hope, The Empire Strikes Back, Return of the Jedi	male	brown	180	Corellia	80	Han Solo	fair		Millennium Falcon, Imperial shuttle	
6	52BBY	blue	A New Hope, Attack of the Clones, Revenge of the Sith	male	brown, grey	178	Tatooine	120	Owen Lars	light			
10	57BBY	blue-gray	A New Hope, Attack of the Clones	male	auburn, white	182	Stewjon	77	Obi-Wan Kenobi	fair		Jedi starfighter, Trade Federation cruiser, Naboo star skiff, Jedi Interceptor, Belbullab-22 starfighter	Tribubble bongo
27	41BBY	orange	Return of the Jedi	male	none	180	Mon Cala	83	Ackbar	brown mottle	Mon Calamari		
33	unknown	red	The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	none	191	Cato Neimoidia	90	Nute Gunray	mottled green	Neimodian		
18	21BBY	hazel	A New Hope, The Empire Strikes Back, Return of the Jedi	male	brown	170	Corellia	77	Wedge Antilles	fair		X-wing	Snowspeeder
35	46BBY	brown	The Phantom Menace, Attack of the Clones, Revenge of the Sith	female	brown	185	Naboo	45	Padmé Amidala	light		Naboo fighter, H-type Nubian yacht, Naboo star skiff	
24	53BBY	red	The Empire Strikes Back	male	none	190	Trandosha	113	Bossk	green	Trandoshan		
21	82BBY	yellow	The Empire Strikes Back, Return of the Jedi, The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	grey	170	Naboo	75	Palpatine	pale			
3	33BBY	red	A New Hope, The Empire Strikes Back, Return of the Jedi, The Phantom Menace, Revenge of the Sith	n/a	n/a	96	Naboo	32	R2-D2	white, blue	Droid		
25	31BBY	brown	Return of the Jedi	male	black	177	Socorro	79	Lando Calrissian	dark		Millennium Falcon	
22	31.5BBY	brown	The Empire Strikes Back, Return of the Jedi, Attack of the Clones	male	black	183	Kamino	78.2	Boba Fett	fair		Slave 1	
23	15BBY	red	The Empire Strikes Back	none	none	200	unknown	140	IG-88	metal	Droid		
15	44BBY	black	A New Hope	male	n/a	173	\N	74	Greedo	green	Rodian		
12	64BBY	blue	Revenge of the Sith	male	auburn, grey	180	Eriadu	unknown	Wilhuff Tarkin	fair			
4	41.9BBY	yellow	The Empire Strikes Back, Revenge of the Sith	male	none	202	Tatooine	136	Darth Vader	white		TIE Advanced x1	
26	37BBY	blue	The Empire Strikes Back	male	none	175	Bespin	79	Lobot	light			
36	52BBY	orange	The Phantom Menace, Attack of the Clones	male	none	196	Naboo	66	Jar Jar Binks	orange	Gungan		
57	unknown	yellow	The Phantom Menace	male	none	264	Quermia	unknown	Yarael Poof	white	Quermian		
13	200BBY	blue	A New Hope, The Empire Strikes Back, Return of the Jedi, Revenge of the Sith	male	brown	228	Kashyyyk	112	Chewbacca	unknown	Wookie	Millennium Falcon	AT-ST
40	unknown	yellow	The Phantom Menace, Attack of the Clones	male	black	137	Toydaria	unknown	Watto	blue, grey	Toydarian		
37	unknown	orange	The Phantom Menace	male	none	224	Naboo	82	Roos Tarpals	grey	Gungan		
11	41.9BBY	blue	The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	blond	188	Tatooine	84	Anakin Skywalker	fair		Trade Federation cruiser, Jedi Interceptor	Zephyr-G swoop bike, XJ-6 airspeeder
28	48BBY	blue	Return of the Jedi	female	auburn	150	Chandrila	unknown	Mon Mothma	fair			
32	92BBY	blue	The Phantom Menace	male	brown	193	unknown	89	Qui-Gon Jinn	fair			Tribubble bongo
47	unknown	unknown	The Phantom Menace	male	none	79	Aleen Minor	15	Ratts Tyerel	grey, blue	Aleena		
29	unknown	brown		male	brown	unknown	unknown	unknown	Arvel Crynyd	fair			
41	unknown	orange	The Phantom Menace	male	none	112	Malastare	40	Sebulba	grey, red	Dug		
59	unknown	blue	The Phantom Menace, Attack of the Clones	male	none	196	Champala	unknown	Mas Amedda	blue	Chagrian		
46	48BBY	hazel	The Phantom Menace, Attack of the Clones, Revenge of the Sith	female	none	178	Ryloth	55	Ayla Secura	blue	Twi'lek		
51	72BBY	brown	The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	none	188	Haruun Kal	84	Mace Windu	dark			
50	unknown	orange	The Phantom Menace	male	none	163	Tund	65	Ben Quadinaros	grey, green, yellow	Toong		
58	22BBY	black	The Phantom Menace, Revenge of the Sith	male	none	188	Dorin	80	Plo Koon	orange	Kel Dor	Jedi starfighter	
52	92BBY	yellow	The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	white	198	Cerea	82	Ki-Adi-Mundi	pale	Cerean		
62	82BBY	blue	Attack of the Clones	male	brown	183	\N	unknown	Cliegg Lars	fair			
2	112BBY	yellow	A New Hope, The Empire Strikes Back, Return of the Jedi, The Phantom Menace, Attack of the Clones, Revenge of the Sith	n/a	n/a	167	Tatooine	75	C-3PO	gold	Droid		
8	unknown	red		n/a	n/a	97	Tatooine	32	R5-D4	white, red	Droid		
16	600BBY	orange	A New Hope, Return of the Jedi, The Phantom Menace	hermaphrodite	n/a	175	Nal Hutta	1,358	Jabba Desilijic Tiure	green-tan, brown	Hutt		
31	unknown	black	Return of the Jedi	male	none	160	Sullust	68	Nien Nunb	grey	Sullustan	Millennium Falcon	
39	unknown	blue	The Phantom Menace	male	brown	183	Naboo	unknown	Ric Olié	fair		Naboo Royal Starship	
45	unknown	pink	Return of the Jedi	male	none	180	Ryloth	unknown	Bib Fortuna	pale	Twi'lek		
38	unknown	orange	The Phantom Menace	male	none	206	Naboo	unknown	Rugor Nass	green	Gungan		
44	54BBY	yellow	The Phantom Menace	male	none	175	Dathomir	80	Darth Maul	red	Zabrak	Scimitar	Sith speeder
76	unknown	unknown	Attack of the Clones	male	none	193	Skako	48	Wat Tambor	green, grey	Skakoan		
67	102BBY	brown	Attack of the Clones, Revenge of the Sith	male	white	193	Serenno	80	Dooku	fair	Human		Flitknot speeder
82	unknown	white	Attack of the Clones, Revenge of the Sith	female	none	178	Umbara	48	Sly Moore	pale			
81	unknown	brown	A New Hope, Revenge of the Sith	male	brown	188	Alderaan	79	Raymus Antilles	light			
75	unknown	red, blue	Attack of the Clones, Revenge of the Sith	female	none	96	unknown	unknown	R4-P17	silver, red			
54	unknown	brown	The Phantom Menace, Revenge of the Sith	male	black	171	Iridonia	unknown	Eeth Koth	brown	Zabrak		
66	unknown	brown	Attack of the Clones	female	brown	165	\N	unknown	Dormé	light	Human		
80	unknown	blue	Revenge of the Sith	male	brown	234	Kashyyyk	136	Tarfful	brown	Wookie		
77	unknown	gold	Attack of the Clones	male	none	191	Muunilinst	unknown	San Hill	grey	Muun		
79	unknown	green, yellow	Revenge of the Sith	male	none	216	Kalee	159	Grievous	brown, white	Kaleesh	Belbullab-22 starfighter	Tsmeu-6 personal wheel bike
78	unknown	black	Attack of the Clones, Revenge of the Sith	female	none	178	Shili	57	Shaak Ti	red, blue, white	Togruta		
73	unknown	black	Attack of the Clones	female	none	213	Kamino	unknown	Taun We	grey	Kaminoan		
34	91BBY	blue	The Phantom Menace	male	blond	170	Coruscant	unknown	Finis Valorum	fair			
42	62BBY	brown	The Phantom Menace	male	black	183	Naboo	unknown	Quarsh Panaka	dark			
43	72BBY	brown	The Phantom Menace, Attack of the Clones	female	black	163	Tatooine	unknown	Shmi Skywalker	fair			
49	unknown	black	The Phantom Menace	male	none	122	Troiken	unknown	Gasgano	white, blue	Xexto		
53	unknown	black	The Phantom Menace, Attack of the Clones, Revenge of the Sith	male	none	196	Glee Anselm	87	Kit Fisto	green	Nautolan		
56	unknown	orange	The Phantom Menace, Revenge of the Sith	male	none	188	Iktotch	unknown	Saesee Tiin	pale	Iktotchi		
48	unknown	yellow		male	none	94	Vulpter	45	Dud Bolt	blue, grey	Vulptereen		
60	unknown	brown	Attack of the Clones	male	black	185	Naboo	85	Gregar Typho	dark		Naboo fighter	
61	unknown	brown	Attack of the Clones	female	brown	157	Naboo	unknown	Cordé	light			
63	unknown	yellow	Attack of the Clones, Revenge of the Sith	male	none	183	Geonosis	80	Poggle the Lesser	green	Geonosian		
65	40BBY	blue	Attack of the Clones	female	black	166	Mirial	50	Barriss Offee	yellow	Mirialan		
69	66BBY	brown	Attack of the Clones	male	black	183	Concord Dawn	79	Jango Fett	tan			
55	unknown	blue	The Phantom Menace, Revenge of the Sith	female	none	184	\N	50	Adi Gallia	dark	Tholothian		
64	58BBY	blue	Attack of the Clones, Revenge of the Sith	female	black	170	Mirial	56.2	Luminara Unduli	yellow	Mirialan		
68	67BBY	brown	Attack of the Clones, Revenge of the Sith	male	black	191	Alderaan	unknown	Bail Prestor Organa	tan	Human		
70	unknown	yellow	Attack of the Clones	female	blonde	168	Zolan	55	Zam Wesell	fair, green, yellow	Clawdite		Koro-2 Exodrive airspeeder
74	unknown	blue	Attack of the Clones	female	white	167	Coruscant	unknown	Jocasta Nu	fair	Human		
72	unknown	black	Attack of the Clones	male	none	229	Kamino	88	Lama Su	grey	Kaminoan		
71	unknown	yellow	Attack of the Clones	male	none	198	Ojom	102	Dexter Jettster	brown	Besalisk		
\.


--
-- Name: characters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.characters_id_seq', 1, false);


--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

