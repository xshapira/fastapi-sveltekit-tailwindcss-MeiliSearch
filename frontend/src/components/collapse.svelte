<script lang="ts">
  export let title: string
  export let description: string
  export let link: string
  export let linkText: string
</script>

<div
  tabindex="0"
  class="collapse max-w-screen-lg min-w-full border rounded-box border-base-300 collapse-arrow my-4"
>
  <div class="collapse-title text-xl font-medium">
    {title}
  </div>
  {#if link && linkText}
    <div class="collapse-content">
      <p class="inline">{description}</p>
      <p class="inline link link-hover" on:click={() => window.open(link)}>
        {linkText}
      </p>
      .
    </div>
  {:else}
    <div class="collapse-content">
      <p>{description}</p>
    </div>
  {/if}
</div>
