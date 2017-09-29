package model

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id

@Entity
data class Person(@Id @GeneratedValue val id: Long, val lastName: String, val firstName: String, val age: Int)