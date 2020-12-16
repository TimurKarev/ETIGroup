<template>
  <div class="full-control">
    <div class="list">
      <md-list>
        <md-list-item md-expand
        v-for="num in this.chlist_data" :key="num.order_num">
          <span class="md-list-item-text">
                {{num.order_num}}
          </span>
          <md-list slot="md-expand">
            <md-list-item class="md-inset" v-for=" i in item_names" :key="i.item" >
              {{ i.item }}
            </md-list-item>
          </md-list>
        </md-list-item>
      </md-list>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'checklists_list',
    props: ['chlist_data'],
    data: function() {
      console.log(this.chlist_data)
      return {
        item_names: [
          {'item': "Стройка"},
          {'item': "Электрика"},
          {'item': "Tелемеханика"},
          {'item': "Документы"},
          {'item': "ЗИП"},
          {'item': "Заказчик"},
        ],
      }
    },
  }
</script>

<style lang="scss" scoped>
  $list-width: 320px;

  .full-control {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap-reverse;
  }

  .list {
    width: $list-width;
  }

  .full-control > .md-list {
    width: $list-width;
    max-width: 100%;
    height: 400px;
    display: inline-block;
    overflow: auto;
    border: 1px solid rgba(#000, .12);
    vertical-align: top;
  }

  .control {
    min-width: 250px;
    display: flex;
    flex-direction: column;
    padding: 16px;
  }
</style>