// selfHTMLElement.js

///////////////////////////////////////////////////////////

// On crée une classe qui hérite de HTMLElement (ou HTMLButtonElement pour un bouton personnalisé).

class SelfHTMLElement extends HTMLButtonElement {}

class FuckTeah extends HTMLElement {

    // initialisation
    constructor() {
        super();
    }

    // exécutée quand l’élément est inséré dans le DOM.
    connectedCallback() {
        //
    }

    // exécutée quand l’élément est retiré.
    disconnectedCallback() {
        //
    }

    // exécutée quand un attribut change.
    attributeChangedCallback() {
        //
    }

    // render 
}


// Enregistrement de la balise personnalisée
customElements.define('my-card', MyCard);


