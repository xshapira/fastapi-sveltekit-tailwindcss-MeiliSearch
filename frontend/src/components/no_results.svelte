<script lang="ts">
  import { onMount } from "svelte"
  import { fade } from "svelte/transition"
  import type { Genre } from "../types"

  export let currentProviders: string[]
  export let currentGenres: Genre[]
  export let input: string
</script>

<div in:fade={{ duration: 200 }} class="flex flex-col mt-20">
  <div class="m-auto text-center max-w-md">
    <p>No results for:</p>
    <p><b><i>{input ? input : "<No input>"}</i></b></p>
    {#if currentGenres.length > 0}
      <p class="pt-2">Genres:</p>
      {#each currentGenres as genre}
        <div class="badge mx-1">{genre.label}</div>
      {/each}
      <p class="text-xs pt-1"><i>Consider using less genres</i></p>
    {/if}
    {#if currentProviders.length > 0}
      <p class="pt-2">Providers:</p>
      {#each currentProviders as provider}
        <div class="badge mx-1">{provider.label}</div>
      {/each}
      <p class="text-xs pt-1">
        <i>Consider adding more providers or removing all</i>
      </p>
    {/if}
  </div>
</div>
