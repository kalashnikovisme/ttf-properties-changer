# ttf-properties-changer
Change properties of ttf-fonts

## Usage

**You need [docker](https://docs.docker.com/engine/install/) to be installed**

1. Clone this repo OR download `.zip` [here](https://github.com/kalashnikovisme/ttf-properties-changer/archive/refs/heads/main.zip) and unarchive it
2. Open Terminal
3. `cd ttf-properties-changer`
4. Run `./ttf-properties-change FILE XML_KEY ATTRIBUTE VALUE`. Now you have new `ttf` file in current directory.

Example:

```bash
./ttf-properties-change ~/Downloads/martian-mono-0.9.2-ttf/MartianMono-CnxBd.ttf "/post/isFixedPitch" value 1
```

Change properties in a several files

```bash
for file in $(find .ttf ~/Downloads/martian-mono-0.9.2-ttf/) do
  ./ttf-properties-change $file "/post/isFixedPitch" value 1
done
```
