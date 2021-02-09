package com.fjgarcia.whisperdeck

import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class DeckItem(val name: String, val ageDays: Int)

class DeckAdapter(private val onClick: (DeckItem) -> Unit) :
    RecyclerView.Adapter<DeckAdapter.Holder>() {

