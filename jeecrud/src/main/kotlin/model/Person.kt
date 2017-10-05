package model

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id


/**
 * @author Markus Reichl
 * @version 05.10.2017
 *
 * Person Entity class using a generated primary key
 */
@Entity
data class Person(@Id @GeneratedValue var id: Long?, var lastName: String, var firstName: String, var age: Int) {
    /**
     * Returns the persons full name as a string
     * @return Firstname Lastname
     */
    override fun toString(): String {
        return firstName + " " + lastName
    }
}