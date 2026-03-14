
// Copie dans le presse-papiers
navigator.clipboard.writeText("Bonjour depuis le web !").then(() => {
    console.log("Texte copié !");
});

// Lecture du presse-papiers
navigator.clipboard.readText().then(text => {
    console.log("Le texte du presse-papiers est :", text);
}).catch(err => {
    console.error("Impossible de lire le presse-papiers :", err);
});
