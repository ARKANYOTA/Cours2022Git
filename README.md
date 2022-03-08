# Cours2022Git
Mes cours de terminal au lycée. En tant que français.

## Web
Pour avoir la version web(même si elle est degulasse) mais pour pour les non-dev sa passe: https://arkanyota.github.io/Cours2022Git/

## Ce que j'utilise
L'app qui gère tout: [github.com/ARKANYOTA/ay-vim-note](https://github.com/ARKANYOTA/ay-vim-note)

Pour éditer j'utilise vim(config [github.com/ARKANYOTA/dotfiles](https://github.com/ARKANYOTA/dotfiles))

Et pour voir les Katex Math: [Notable.app](https://notable.app)

## Render mes cours
[github.com/ARKANYOTA/markdownToHtmlEnNodeJs](https://github.com/ARKANYOTA/markdownToHtmlEnNodeJs)
```bash
node ~/markdowntohtml/index.js -i ~/Cours2022Git/notes/ -o ~/Cours2022Git/output --choosetheme --setinfolder ./exports --toc --render-math --dark --linker && ./exportall.sh 
```

## Pour édit
[github.com/ARKANYOTA/CoursEditor](https://github.com/ARKANYOTA/CoursEditor)
