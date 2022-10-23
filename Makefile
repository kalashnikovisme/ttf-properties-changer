build:
	docker build . -t fonttools

to_ttx:
	sudo rm MartianMono-CnBd*.ttx && docker run --volume ${PWD}:/usr/share/ fonttools ttx -d /usr/share/ /usr/share/MartianMono-CnBd.ttf && sudo chown pavel MartianMono-CnBd.ttx

to_ttf:
	docker run --volume ${PWD}:/usr/share/ fonttools ttx -o /usr/share/MartianMono-CnBd-fixed.ttf /usr/share/MartianMono-CnBd.ttx && sudo chown pavel MartianMono-CnBd-fixed.ttf

replace:
	docker run --volume ${PWD}:/usr/share/ fonttools python /usr/share/change.py /usr/share/MartianMono-CnBd.ttx 
