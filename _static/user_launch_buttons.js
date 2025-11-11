let _button_data = {"buttons": [{"type": "dropdown", "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-globe\" viewBox=\"0 0 16 16\"> <path d=\"M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m7.5-6.923c-.67.204-1.335.82-1.887 1.855A8 8 0 0 0 5.145 4H7.5zM4.09 4a9.3 9.3 0 0 1 .64-1.539 7 7 0 0 1 .597-.933A7.03 7.03 0 0 0 2.255 4zm-.582 3.5c.03-.877.138-1.718.312-2.5H1.674a7 7 0 0 0-.656 2.5zM4.847 5a12.5 12.5 0 0 0-.338 2.5H7.5V5zM8.5 5v2.5h2.99a12.5 12.5 0 0 0-.337-2.5zM4.51 8.5a12.5 12.5 0 0 0 .337 2.5H7.5V8.5zm3.99 0V11h2.653c.187-.765.306-1.608.338-2.5zM5.145 12q.208.58.468 1.068c.552 1.035 1.218 1.65 1.887 1.855V12zm.182 2.472a7 7 0 0 1-.597-.933A9.3 9.3 0 0 1 4.09 12H2.255a7 7 0 0 0 3.072 2.472M3.82 11a13.7 13.7 0 0 1-.312-2.5h-2.49c.062.89.291 1.733.656 2.5zm6.853 3.472A7 7 0 0 0 13.745 12H11.91a9.3 9.3 0 0 1-.64 1.539 7 7 0 0 1-.597.933M8.5 12v2.923c.67-.204 1.335-.82 1.887-1.855q.26-.487.468-1.068zm3.68-1h2.146c.365-.767.594-1.61.656-2.5h-2.49a13.7 13.7 0 0 1-.312 2.5m2.802-3.5a7 7 0 0 0-.656-2.5H12.18c.174.782.282 1.623.312 2.5zM11.27 2.461c.247.464.462.98.64 1.539h1.835a7 7 0 0 0-3.072-2.472c.218.284.418.598.597.933M10.855 4a8 8 0 0 0-.468-1.068C9.835 1.897 9.17 1.282 8.5 1.077V4z\"/> </svg>", "items": [{"label": "English", "url": "https://giscience.github.io/gis-training-resource-center/content/EN"}, {"label": "Espa\u00f1ol", "url": "https://giscience.github.io/gis-training-resource-center/content/ES"}]}]};

// Css to let the dropdown open on hover
const dropdownCSS = `
/* Custom CSS to make the dropdown open on hover */
.dropdown-menu {
display: none; /* Hide the dropdown menu by default */
}
.dropdown-source-buttons:hover .dropdown-menu {
display: block; /* Display the dropdown menu on hover */
}
`

// MAIN => hook into the DOM and add the buttons
document.addEventListener('DOMContentLoaded', () => addButtons(_button_data["buttons"]));

// distribute based on the type of the buttons
let addButtons = (buttons) => {
    // Append launch buttons to the page
    buttons.forEach(function(button) {
        element = button.type == "dropdown" ? addDropdown(button) : addButton(button);
        document.getElementsByClassName('article-header-buttons')[0].prepend(element)
    });
    console.log("[custom-launch-buttons] end of setup")
}

/* Structure of dropdown: 
*  <div>
*       <button>
*       <ul> 
*           <li> <a> </li>
*       </ul>
*  </div>
*/
let addDropdown = (button) => {
    // Create a new container for full element
    let container = document.createElement('div');
    container.classList.add("dropdown", "dropdown-source-buttons");

    // Create a new <style> element
    var style = document.createElement('style');
    if (style.styleSheet) {
        // For IE
        style.styleSheet.cssText = dropdownCSS;
    } else {
        // For other browsers
        style.appendChild(document.createTextNode(dropdownCSS));
    }
    container.appendChild(style);

    // Create a new button element and set necessary elements
    let buttonElement = document.createElement('button');
    buttonElement.classList.add("btn", "dropdown-toggle");
    buttonElement.setAttribute("data-bs-toggle", "dropdown");

    if(button.icon != undefined) buttonElement.appendChild(setIcon(button.icon)); 
    if(button.label!= undefined) buttonElement.innerHTML += " " + button.label

    // Create dropdown list containing all links
    let dropdownList = document.createElement('ul');
    dropdownList.classList.add("dropdown-menu");

    // Add dropdown items to the list according to the given format
    // create <li> which will contain <a> with all the relevant information (b for button, running out of names...)
    button.items.forEach(function(b) {
        let listItem = document.createElement('li');
        let linkItem = document.createElement('a');
        linkItem.classList.add("btn", "btn-sm", "dropdown-item");
        linkItem.setAttribute("data-bs-placement", "left");
        linkItem.href = b.url;
        console.log("[launch-button] URL added : " + b.url); 

        // Check if icon is present, if not add a dot (&#x2022;)
        if(b.icon != undefined){
            let icon = setSubIcon(b.icon)
            linkItem.appendChild(icon);
        } else {
            linkItem.innerHTML += "&#x2022;";
        }
        if(b.label != undefined) linkItem.innerHTML += " " + b.label;

        listItem.appendChild(linkItem);
        dropdownList.appendChild(listItem);
    })
    
    container.appendChild(buttonElement);
    container.appendChild(dropdownList);

    return container
}

// Function which will return a button element with all the relevant information
let addButton = (button) => {
    // Create a new button element
    var buttonElement = document.createElement('button');

    // Set the button's text and class
    buttonElement.classList.add("btn", "btn-sm", "navbar-btn");
    if (button.icon != undefined) buttonElement.innerHTML += button.icon;
    if (button.label != undefined) buttonElement.innerHTML += " " + button.label;
    
    // Add an event listener to the button
    buttonElement.addEventListener('click', function() {
        // Execute the specified action when the button is clicked
        console.log("[launch-button] URL clicked : " + button.link); 
        window.location.href = button.link;
    });
    console.log("[launch-button] URL added : " + button.link); 

    // Add the button to the page
    return buttonElement
}


// Function which sets the same classes for all svg icons
const setIcon = (icon) => {
    // Create a new DOMParser
    const parser = new DOMParser();
    const element = parser.parseFromString(icon, 'text/html').getElementsByTagName('svg')[0];
    element.classList = []
    element.classList.add("svg-inline--fa")
    return element
}

// Different function for svg icons living in different places ;) 
const setSubIcon = (icon) => {
    let span = document.createElement('span');
    span.classList.add("btn__icon-container");
    span.appendChild( setIcon(icon) );
    return span
}
