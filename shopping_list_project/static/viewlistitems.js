$(function() {
    initDataToJavaScript();
});

function initDataToJavaScript() {
    let fetchData = $('#vueapp1').attr('data-to-js')
    if (fetchData != undefined || fetchData != null) {
        let data = JSON.parse(fetchData);
        viewListItemsVue.dataFromBackend = data; 
    }
}

let viewListItemsVue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#vueapp1',
    data: {
        dataFromBackend: {},
        listItemsInput: '',
        newListItemError: ''
    },
    methods: {
        delListItem(e) {
            let clickedIndex = e.target.dataset.index;
            this.dataFromBackend[0].splice(clickedIndex,1);
        },
        addNewListsItem() {
            if (this.listItemsInput.length > 2) {
                this.dataFromBackend[0].push(this.listItemsInput)
                this.listItemsInput = ''
                this.newListItemError = ''
            } else {
                this.newListItemError = 'At least 3 characters required.'
            }
            
        }
    }
})
//click-kel megyünk tovább, törlés kell